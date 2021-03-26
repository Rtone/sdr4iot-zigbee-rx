/**
 * Copyright (c) 2018, Nordic Semiconductor ASA
 *
 * All rights reserved.
 *
 * Redistribution and use in source and binary forms, with or without modification,
 * are permitted provided that the following conditions are met:
 *
 * 1. Redistributions of source code must retain the above copyright notice, this
 *    list of conditions and the following disclaimer.
 *
 * 2. Redistributions in binary form, except as embedded into a Nordic
 *    Semiconductor ASA integrated circuit in a product or a software update for
 *    such product, must reproduce the above copyright notice, this list of
 *    conditions and the following disclaimer in the documentation and/or other
 *    materials provided with the distribution.
 *
 * 3. Neither the name of Nordic Semiconductor ASA nor the names of its
 *    contributors may be used to endorse or promote products derived from this
 *    software without specific prior written permission.
 *
 * 4. This software, with or without modification, must only be used with a
 *    Nordic Semiconductor ASA integrated circuit.
 *
 * 5. Any software provided in binary form under this license must not be reverse
 *    engineered, decompiled, modified and/or disassembled.
 *
 * THIS SOFTWARE IS PROVIDED BY NORDIC SEMICONDUCTOR ASA "AS IS" AND ANY EXPRESS
 * OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES
 * OF MERCHANTABILITY, NONINFRINGEMENT, AND FITNESS FOR A PARTICULAR PURPOSE ARE
 * DISCLAIMED. IN NO EVENT SHALL NORDIC SEMICONDUCTOR ASA OR CONTRIBUTORS BE
 * LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
 * CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE
 * GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
 * HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
 * LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT
 * OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
 *
 */
/** @file
 *
 * @defgroup zigbee_examples_light_switch main.c
 * @{
 * @ingroup zigbee_examples
 * @brief Dimmer switch for HA profile implementation.
 */

#include "zboss_api.h"
#include "zb_mem_config_min.h"
#include "zb_error_handler.h"

#include "app_timer.h"
#include "bsp.h"
#include "boards.h"

#include "nrf_log.h"
#include "nrf_log_ctrl.h"
#include "nrf_log_default_backends.h"

#define IEEE_CHANNEL_MASK                   (1l << ZIGBEE_CHANNEL)              /**< Scan only one, predefined channel to find the coordinator. */
#define LIGHT_SWITCH_ENDPOINT               1                                   /**< Source endpoint used to control light bulb. */
#define MATCH_DESC_REQ_START_DELAY          (2 * ZB_TIME_ONE_SECOND)            /**< Delay between the light switch startup and light bulb finding procedure. */
#define MATCH_DESC_REQ_TIMEOUT              (5 * ZB_TIME_ONE_SECOND)            /**< Timeout for finding procedure. */
#define MATCH_DESC_REQ_ROLE                 ZB_NWK_BROADCAST_RX_ON_WHEN_IDLE    /**< Find only non-sleepy device. */
#define ERASE_PERSISTENT_CONFIG             ZB_FALSE                            /**< Do not erase NVRAM to save the network parameters after device reboot or power-off. NOTE: If this option is set to ZB_TRUE then do full device erase for all network devices before running other samples. */
#define ZIGBEE_NETWORK_STATE_LED            BSP_BOARD_LED_2                     /**< LED indicating that light switch successfully joind ZigBee network. */
#define BULB_FOUND_LED                      BSP_BOARD_LED_3                     /**< LED indicating that light witch found a light bulb to control. */
#define LIGHT_SWITCH_BUTTON_ON              BSP_BOARD_BUTTON_0                  /**< Button ID used to switch on the light bulb. */
#define LIGHT_SWITCH_BUTTON_OFF             BSP_BOARD_BUTTON_1                  /**< Button ID used to switch off the light bulb. */
#define SLEEPY_ON_BUTTON                    BSP_BOARD_BUTTON_2                  /**< Button ID used to determine if we need the sleepy device behaviour (pressed means yes). */

#define LIGHT_SWITCH_DIMM_STEP              15                                  /**< Dim step size - increases/decreses current level (range 0x000 - 0xfe). */
#define LIGHT_SWITCH_DIMM_TRANSACTION_TIME  2                                   /**< Transition time for a single step operation in 0.1 sec units. 0xFFFF - immediate change. */

#define LIGHT_SWITCH_BUTTON_THRESHOLD       ZB_TIME_ONE_SECOND                      /**< Number of beacon intervals the button should be pressed to dimm the light bulb. */
#define LIGHT_SWITCH_BUTTON_SHORT_POLL_TMO  ZB_MILLISECONDS_TO_BEACON_INTERVAL(50)  /**< Delay between button state checks used in order to detect button long press. */
#define LIGHT_SWITCH_BUTTON_LONG_POLL_TMO   ZB_MILLISECONDS_TO_BEACON_INTERVAL(300) /**< Time after which the button state is checked again to detect button hold - the dimm command is sent again. */

#if !defined ZB_ED_ROLE
#error Define ZB_ED_ROLE to compile light switch (End Device) source code.
#endif


typedef struct light_switch_bulb_params_s
{
  zb_uint8_t  endpoint;
  zb_uint16_t short_addr;
} light_switch_bulb_params_t;

typedef struct light_switch_button_s
{
  zb_bool_t in_progress;
  zb_time_t timestamp;
} light_switch_button_t;

typedef struct light_switch_ctx_s
{
  light_switch_bulb_params_t bulb_params;
  light_switch_button_t      button;
} light_switch_ctx_t;


static zb_void_t find_light_bulb_timeout(zb_uint8_t param);

static light_switch_ctx_t m_device_ctx;
static zb_uint8_t         m_attr_zcl_version   = ZB_ZCL_VERSION;
static zb_uint8_t         m_attr_power_source  = ZB_ZCL_BASIC_POWER_SOURCE_UNKNOWN;
static zb_uint16_t        m_attr_identify_time = 0;

/* Declare attribute list for Basic cluster. */
ZB_ZCL_DECLARE_BASIC_ATTRIB_LIST(basic_attr_list, &m_attr_zcl_version, &m_attr_power_source);

/* Declare attribute list for Identify cluster. */
ZB_ZCL_DECLARE_IDENTIFY_ATTRIB_LIST(identify_attr_list, &m_attr_identify_time);

/* Declare cluster list for Dimmer Switch device (Identify, Basic, Scenes, Groups, On Off, Level Control). */
/* Only clusters Identify and Basic have attributes. */
ZB_HA_DECLARE_DIMMER_SWITCH_CLUSTER_LIST(dimmer_switch_clusters,
                                         basic_attr_list,
                                         identify_attr_list);

/* Declare endpoint for Dimmer Switch device. */
ZB_HA_DECLARE_DIMMER_SWITCH_EP(dimmer_switch_ep,
                               LIGHT_SWITCH_ENDPOINT,
                               dimmer_switch_clusters);

/* Declare application's device context (list of registered endpoints) for Dimmer Switch device. */
ZB_HA_DECLARE_DIMMER_SWITCH_CTX(dimmer_switch_ctx, dimmer_switch_ep);

/**@brief Function for the Timer initialization.
 *
 * @details Initializes the timer module. This creates and starts application timers.
 */
static void timers_init(void)
{
    ret_code_t err_code;

    // Initialize timer module.
    err_code = app_timer_init();
    APP_ERROR_CHECK(err_code);
}

/**@brief Function for initializing the nrf log module.
 */
static void log_init(void)
{
    ret_code_t err_code = NRF_LOG_INIT(NULL);
    APP_ERROR_CHECK(err_code);

    NRF_LOG_DEFAULT_BACKENDS_INIT();
}

/**@brief Function for sending ON/OFF requests to the light bulb.
 *
 * @param[in]   param    Non-zero reference to ZigBee stack buffer that will be used to construct on/off request.
 * @param[in]   on_off   Requested state of the light bulb.
 */
static zb_void_t light_switch_send_on_off(zb_uint8_t param, zb_uint16_t on_off)
{
    zb_uint8_t           cmd_id;
    zb_buf_t           * p_buf = ZB_BUF_FROM_REF(param);

    if (on_off)
    {
        cmd_id = ZB_ZCL_CMD_ON_OFF_ON_ID;
    }
    else
    {
        cmd_id = ZB_ZCL_CMD_ON_OFF_OFF_ID;
    }

    NRF_LOG_INFO("Send ON/OFF command: %d", on_off);

    ZB_ZCL_ON_OFF_SEND_REQ(p_buf,
                           m_device_ctx.bulb_params.short_addr,
                           ZB_APS_ADDR_MODE_16_ENDP_PRESENT,
                           m_device_ctx.bulb_params.endpoint,
                           LIGHT_SWITCH_ENDPOINT,
                           ZB_AF_HA_PROFILE_ID,
                           ZB_ZCL_DISABLE_DEFAULT_RESPONSE,
                           cmd_id,
                           NULL);
}

/**@brief Function for sending step requests to the light bulb.
 *
 * @param[in]   param        Non-zero reference to ZigBee stack buffer that will be used to construct step request.
 * @param[in]   is_step_up   Boolean parameter selecting direction of step change.
 */
static zb_void_t light_switch_send_step(zb_uint8_t param, zb_uint16_t is_step_up)
{
    zb_uint8_t           step_dir;
    zb_buf_t           * p_buf = ZB_BUF_FROM_REF(param);

    if (is_step_up)
    {
        step_dir = ZB_ZCL_LEVEL_CONTROL_STEP_MODE_UP;
    }
    else
    {
        step_dir = ZB_ZCL_LEVEL_CONTROL_STEP_MODE_DOWN;
    }

    NRF_LOG_INFO("Send step level command: %d", is_step_up);

    ZB_ZCL_LEVEL_CONTROL_SEND_STEP_REQ(p_buf,
                                       m_device_ctx.bulb_params.short_addr,
                                       ZB_APS_ADDR_MODE_16_ENDP_PRESENT,
                                       m_device_ctx.bulb_params.endpoint,
                                       LIGHT_SWITCH_ENDPOINT,
                                       ZB_AF_HA_PROFILE_ID,
                                       ZB_ZCL_DISABLE_DEFAULT_RESPONSE,
                                       NULL,
                                       step_dir,
                                       LIGHT_SWITCH_DIMM_STEP,
                                       LIGHT_SWITCH_DIMM_TRANSACTION_TIME);
}

/**@brief Perform local operation - leave network.
 *
 * @param[in]   param   Reference to ZigBee stack buffer that will be used to construct leave request.
 */
static void light_switch_leave_nwk(zb_uint8_t param)
{
    zb_ret_t zb_err_code;

    /* We are going to leave */
    if (param)
    {
        zb_buf_t                  * p_buf = ZB_BUF_FROM_REF(param);
        zb_zdo_mgmt_leave_param_t * p_req_param;

        p_req_param = ZB_GET_BUF_PARAM(p_buf, zb_zdo_mgmt_leave_param_t);
        UNUSED_RETURN_VALUE(ZB_BZERO(p_req_param, sizeof(zb_zdo_mgmt_leave_param_t)));

        /* Set dst_addr == local address for local leave */
        p_req_param->dst_addr = ZB_PIBCACHE_NETWORK_ADDRESS();
        p_req_param->rejoin   = ZB_FALSE;
        UNUSED_RETURN_VALUE(zdo_mgmt_leave_req(param, NULL));
    }
    else
    {
        zb_err_code = ZB_GET_OUT_BUF_DELAYED(light_switch_leave_nwk);
        ZB_ERROR_CHECK(zb_err_code);
    }
}

/**@brief Function for starting join/rejoin procedure.
 *
 * param[in]   leave_type   Type of leave request (with or without rejoin).
 */
static zb_void_t light_switch_retry_join(zb_uint8_t leave_type)
{
    zb_bool_t comm_status;

    if (leave_type == ZB_NWK_LEAVE_TYPE_RESET)
    {
        comm_status = bdb_start_top_level_commissioning(ZB_BDB_NETWORK_STEERING);
        ZB_COMM_STATUS_CHECK(comm_status);
    }
}

/**@brief Function for leaving current network and starting join procedure afterwards.
 *
 * @param[in]   param   Optional reference to ZigBee stack buffer to be reused by leave and join procedure.
 */
static zb_void_t light_switch_leave_and_join(zb_uint8_t param)
{
    if (ZB_JOINED())
    {
        /* Leave network. Joining procedure will be initiated inisde ZigBee stack signal handler. */
        light_switch_leave_nwk(param);
    }
    else
    {
        /* Already left network. Start joining procedure. */
        light_switch_retry_join(ZB_NWK_LEAVE_TYPE_RESET);

        if (param)
        {
            ZB_FREE_BUF_BY_REF(param);
        }
    }
}

/**@brief Callback function receiving finding procedure results.
 *
 * @param[in]   param   Reference to ZigBee stack buffer used to pass received data.
 */
static zb_void_t find_light_bulb_cb(zb_uint8_t param)
{
    zb_buf_t                   * p_buf  = ZB_BUF_FROM_REF(param);                              // Resolve buffer number to buffer address
    zb_zdo_match_desc_resp_t   * p_resp = (zb_zdo_match_desc_resp_t *) ZB_BUF_BEGIN(p_buf);    // Get the begining of the response
    zb_apsde_data_indication_t * p_ind  = ZB_GET_BUF_PARAM(p_buf, zb_apsde_data_indication_t); // Get the pointer to the parameters buffer, which stores APS layer response
    zb_uint8_t                 * p_match_ep;
    zb_ret_t                     zb_err_code;

    if ((p_resp->status == ZB_ZDP_STATUS_SUCCESS) && (p_resp->match_len > 0) && (!m_device_ctx.bulb_params.short_addr))
    {
        /* Match EP list follows right after response header */
        p_match_ep = (zb_uint8_t *)(p_resp + 1);

        /* We are searching for exact cluster, so only 1 EP may be found */
        m_device_ctx.bulb_params.endpoint   = *p_match_ep;
        m_device_ctx.bulb_params.short_addr = p_ind->src_addr;

        NRF_LOG_INFO("Found bulb addr: %d ep: %d", m_device_ctx.bulb_params.short_addr, m_device_ctx.bulb_params.endpoint);

        zb_err_code = ZB_SCHEDULE_ALARM_CANCEL(find_light_bulb_timeout, ZB_ALARM_ANY_PARAM);
        ZB_ERROR_CHECK(zb_err_code);

        bsp_board_led_on(BULB_FOUND_LED);
    }

    if (param)
    {
        ZB_FREE_BUF_BY_REF(param);
    }
}

/**@brief Function for sending ON/OFF and Level Control find request.
 *
 * @param[in]   param   Non-zero reference to ZigBee stack buffer that will be used to construct find request.
 */
static zb_void_t find_light_bulb(zb_uint8_t param)
{
    zb_buf_t                  * p_buf = ZB_BUF_FROM_REF(param); // Resolve buffer number to buffer address
    zb_zdo_match_desc_param_t * p_req;

    /* Initialize pointers inside buffer and reserve space for zb_zdo_match_desc_param_t request */
    UNUSED_RETURN_VALUE(ZB_BUF_INITIAL_ALLOC(p_buf, sizeof(zb_zdo_match_desc_param_t) + (1) * sizeof(zb_uint16_t), p_req));

    p_req->nwk_addr         = MATCH_DESC_REQ_ROLE;              // Send to devices specified by MATCH_DESC_REQ_ROLE
    p_req->addr_of_interest = MATCH_DESC_REQ_ROLE;              // Get responses from devices specified by MATCH_DESC_REQ_ROLE
    p_req->profile_id       = ZB_AF_HA_PROFILE_ID;              // Look for Home Automation profile clusters

    /* We are searching for 2 clusters: On/Off and Level Control Server */
    p_req->num_in_clusters  = 2;
    p_req->num_out_clusters = 0;
    /*lint -save -e415 // Suppress warning 415 "likely access of out-of-bounds pointer" */
    p_req->cluster_list[0]  = ZB_ZCL_CLUSTER_ID_ON_OFF;
    p_req->cluster_list[1]  = ZB_ZCL_CLUSTER_ID_LEVEL_CONTROL;
    /*lint -restore */
    m_device_ctx.bulb_params.short_addr = 0x00; // Reset short address in order to parse only one response.
    UNUSED_RETURN_VALUE(zb_zdo_match_desc_req(param, find_light_bulb_cb));
}

/**@brief Finding procedure timeout handler.
 *
 * @param[in]   param   Reference to ZigBee stack buffer that will be used to construct find request.
 */
static zb_void_t find_light_bulb_timeout(zb_uint8_t param)
{
    zb_ret_t zb_err_code;

    if (param)
    {
        NRF_LOG_INFO("Bulb not found, try again");
        zb_err_code = ZB_SCHEDULE_ALARM(find_light_bulb, param, MATCH_DESC_REQ_START_DELAY);
        ZB_ERROR_CHECK(zb_err_code);
        zb_err_code = ZB_SCHEDULE_ALARM(find_light_bulb_timeout, 0, MATCH_DESC_REQ_TIMEOUT);
        ZB_ERROR_CHECK(zb_err_code);
    }
    else
    {
        zb_err_code = ZB_GET_OUT_BUF_DELAYED(find_light_bulb_timeout);
        ZB_ERROR_CHECK(zb_err_code);
    }
}

/**@brief Callback for detecting button press duration.
 *
 * @param[in]   button   BSP Button that was pressed.
 */
static zb_void_t light_switch_button_handler(zb_uint8_t button)
{
    zb_time_t current_time;
    zb_bool_t short_expired;
    zb_bool_t on_off;
    zb_ret_t zb_err_code;

    current_time = ZB_TIMER_GET();

    if (button == LIGHT_SWITCH_BUTTON_ON)
    {
        on_off = ZB_TRUE;
    }
    else
    {
        on_off = ZB_FALSE;
    }

    if (ZB_TIME_SUBTRACT(current_time, m_device_ctx.button.timestamp) > LIGHT_SWITCH_BUTTON_THRESHOLD)
    {
        short_expired = ZB_TRUE;
    }
    else
    {
        short_expired = ZB_FALSE;
    }

    /* Check if button was released during LIGHT_SWITCH_BUTTON_SHORT_POLL_TMO. */
    if (!bsp_button_is_pressed(button))
    {
        if (!short_expired)
        {
            /* Allocate output buffer and send on/off command. */
            zb_err_code = ZB_GET_OUT_BUF_DELAYED2(light_switch_send_on_off, on_off);
            ZB_ERROR_CHECK(zb_err_code);
        }

        /* Button released - wait for accept next event. */
        m_device_ctx.button.in_progress = ZB_FALSE;
    }
    else
    {
        if (short_expired)
        {
            /* The button is still pressed - allocate output buffer and send step command. */
            zb_err_code = ZB_GET_OUT_BUF_DELAYED2(light_switch_send_step, on_off);
            ZB_ERROR_CHECK(zb_err_code);
            zb_err_code = ZB_SCHEDULE_ALARM(light_switch_button_handler, button, LIGHT_SWITCH_BUTTON_LONG_POLL_TMO);
            ZB_ERROR_CHECK(zb_err_code);
        }
        else
        {
            /* Wait another LIGHT_SWITCH_BUTTON_SHORT_POLL_TMO, until LIGHT_SWITCH_BUTTON_THRESHOLD will be reached. */
            zb_err_code = ZB_SCHEDULE_ALARM(light_switch_button_handler, button, LIGHT_SWITCH_BUTTON_SHORT_POLL_TMO);
            ZB_ERROR_CHECK(zb_err_code);
        }
    }
}

/**@brief Callback for button events.
 *
 * @param[in]   evt      Incoming event from the BSP subsystem.
 */
static void buttons_handler(bsp_event_t evt)
{
    zb_ret_t zb_err_code;
    zb_uint32_t button;

    if (!m_device_ctx.bulb_params.short_addr)
    {
        /* No bulb found yet. */
        return;
    }

    switch(evt)
    {
        case BSP_EVENT_KEY_0:
            button = LIGHT_SWITCH_BUTTON_ON;
            break;

        case BSP_EVENT_KEY_1:
            button = LIGHT_SWITCH_BUTTON_OFF;
            break;

        default:
            NRF_LOG_INFO("Unhandled BSP Event received: %d", evt);
            return;
    }

    if (!m_device_ctx.button.in_progress)
    {
        m_device_ctx.button.in_progress = ZB_TRUE;
        m_device_ctx.button.timestamp = ZB_TIMER_GET();

        zb_err_code = ZB_SCHEDULE_ALARM(light_switch_button_handler, button, LIGHT_SWITCH_BUTTON_SHORT_POLL_TMO);
        ZB_ERROR_CHECK(zb_err_code);
    }
}

/**@brief Function for initializing LEDs and buttons.
 */
static zb_void_t leds_buttons_init(void)
{
    ret_code_t error_code;

    /* Initialize LEDs and buttons - use BSP to control them. */
    error_code = bsp_init(BSP_INIT_LEDS | BSP_INIT_BUTTONS, buttons_handler);
    APP_ERROR_CHECK(error_code);
    /* By default the bsp_init attaches BSP_KEY_EVENTS_{0-4} to the PUSH events of the corresponding buttons. */

    bsp_board_leds_off();
}

/**@brief Function to set the Sleeping Mode according to the SLEEPY_ON_BUTTON state.
*/
static zb_void_t sleepy_device_setup(void)
{
    zb_set_rx_on_when_idle(bsp_button_is_pressed(SLEEPY_ON_BUTTON) ? ZB_FALSE : ZB_TRUE);
}

/**@brief ZigBee stack event handler.
 *
 * @param[in]   param   Reference to ZigBee stack buffer used to pass arguments (signal).
 */
void zboss_signal_handler(zb_uint8_t param)
{
    zb_zdo_app_signal_hdr_t      * p_sg_p         = NULL;
    zb_zdo_signal_leave_params_t * p_leave_params = NULL;
    zb_zdo_app_signal_type_t       sig            = zb_get_app_signal(param, &p_sg_p);
    zb_ret_t                       status         = ZB_GET_APP_SIGNAL_STATUS(param);
    zb_ret_t                       zb_err_code;

    switch(sig)
    {
        case ZB_BDB_SIGNAL_DEVICE_FIRST_START:
        case ZB_BDB_SIGNAL_DEVICE_REBOOT:
            if (status == RET_OK)
            {
                NRF_LOG_INFO("Joined network successfully");
                bsp_board_led_on(ZIGBEE_NETWORK_STATE_LED);

                /* Check the light device address */
                if (m_device_ctx.bulb_params.short_addr == 0x0000)
                {
                    zb_err_code = ZB_SCHEDULE_ALARM(find_light_bulb, param, MATCH_DESC_REQ_START_DELAY);
                    ZB_ERROR_CHECK(zb_err_code);
                    zb_err_code = ZB_SCHEDULE_ALARM(find_light_bulb_timeout, 0, MATCH_DESC_REQ_TIMEOUT);
                    ZB_ERROR_CHECK(zb_err_code);
                    param = 0; // Do not free buffer - it will be reused by find_light_bulb callback
                }
            }
            else
            {
                NRF_LOG_ERROR("Failed to join network. Status: %d", status);
                bsp_board_led_off(ZIGBEE_NETWORK_STATE_LED);
                zb_err_code = ZB_SCHEDULE_ALARM(light_switch_leave_and_join, 0, ZB_TIME_ONE_SECOND);
                ZB_ERROR_CHECK(zb_err_code);
            }
            break;

        case ZB_ZDO_SIGNAL_LEAVE:
            if (status == RET_OK)
            {
                bsp_board_led_off(ZIGBEE_NETWORK_STATE_LED);
                p_leave_params = ZB_ZDO_SIGNAL_GET_PARAMS(p_sg_p, zb_zdo_signal_leave_params_t);
                NRF_LOG_INFO("Network left. Leave type: %d", p_leave_params->leave_type);
                light_switch_retry_join(p_leave_params->leave_type);
            }
            else
            {
                NRF_LOG_ERROR("Unable to leave network. Status: %d", status);
            }
            break;

        case ZB_COMMON_SIGNAL_CAN_SLEEP:
            {
                zb_zdo_signal_can_sleep_params_t *can_sleep_params = ZB_ZDO_SIGNAL_GET_PARAMS(p_sg_p, zb_zdo_signal_can_sleep_params_t);
                NRF_LOG_INFO("Can sleep for %ld ms", can_sleep_params->sleep_tmo);
                zb_sleep_now();
            }
            break;

        case ZB_ZDO_SIGNAL_PRODUCTION_CONFIG_READY:
            if (status != RET_OK)
            {
                NRF_LOG_WARNING("Production config is not present or invalid");
            }
            break;

        default:
            /* Unhandled signal. For more information see: zb_zdo_app_signal_type_e and zb_ret_e */
            NRF_LOG_INFO("Unhandled signal %d. Status: %d", sig, status);
    }

    if (param)
    {
        ZB_FREE_BUF_BY_REF(param);
    }
}

/**@brief Function for application main entry.
 */
int main(void)
{
    zb_ret_t       zb_err_code;
    zb_ieee_addr_t ieee_addr;

    /* Initialize timers, loging system and GPIOs. */
    timers_init();
    log_init();
    leds_buttons_init();

    /* Set ZigBee stack logging level and traffic dump subsystem. */
    ZB_SET_TRACE_LEVEL(ZIGBEE_TRACE_LEVEL);
    ZB_SET_TRACE_MASK(ZIGBEE_TRACE_MASK);
    ZB_SET_TRAF_DUMP_OFF();

    /* Initialize ZigBee stack. */
    ZB_INIT("light_switch");

    /* Set device address to the value read from FICR registers. */
    zb_osif_get_ieee_eui64(ieee_addr);
    zb_set_long_address(ieee_addr);

    zb_set_network_ed_role(IEEE_CHANNEL_MASK);
    zb_set_nvram_erase_at_start(ERASE_PERSISTENT_CONFIG);

    zb_set_ed_timeout(ED_AGING_TIMEOUT_64MIN);
    zb_set_keepalive_timeout(ZB_MILLISECONDS_TO_BEACON_INTERVAL(3000));
    sleepy_device_setup();

    /* Initialize application context structure. */
    UNUSED_RETURN_VALUE(ZB_MEMSET(&m_device_ctx, 0, sizeof(light_switch_ctx_t)));

    /* Register dimmer switch device context (endpoints). */
    ZB_AF_REGISTER_DEVICE_CTX(&dimmer_switch_ctx);

    /** Start Zigbee Stack. */
    zb_err_code = zboss_start();
    ZB_ERROR_CHECK(zb_err_code);

    while(1)
    {
        zboss_main_loop_iteration();
        UNUSED_RETURN_VALUE(NRF_LOG_PROCESS());
    }
}


/**
 * @}
 */
