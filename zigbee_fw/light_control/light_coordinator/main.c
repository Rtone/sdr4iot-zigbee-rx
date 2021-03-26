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
 * @defgroup zigbee_examples_light_coordinator main.c
 * @{
 * @ingroup zigbee_examples
 * @brief Simple ZigBee network coordinator implementation.
 */

#include "zboss_api.h"
#include "zb_mem_config_max.h"
#include "zb_error_handler.h"

#include "boards.h"

#include "nrf_log.h"
#include "nrf_log_ctrl.h"
#include "nrf_log_default_backends.h"

#define ERASE_PERSISTENT_CONFIG           ZB_FALSE                              /**< Do not erase NVRAM to save the network parameters after device reboot or power-off. NOTE: If this option is set to ZB_TRUE then do full device erase for all network devices before running other samples. */
#define MAX_CHILDREN                      10                                    /**< The maximum amount of connected devices. Setting this value to 0 disables association to this device.  */
#define IEEE_CHANNEL_MASK                 (1l << ZIGBEE_CHANNEL)                /**< Scan only one, predefined channel to find the coordinator. */
#ifdef  BOARD_PCA10059                                                          /**< If it is Dongle */
#define ZIGBEE_NETWORK_STATE_LED          BSP_BOARD_LED_0                       /**< LED indicating that network is opened for new nodes. */
#else
#define ZIGBEE_NETWORK_STATE_LED          BSP_BOARD_LED_2                       /**< LED indicating that network is opened for new nodes. */
#endif

#ifndef ZB_COORDINATOR_ROLE
#error Define ZB_COORDINATOR_ROLE to compile coordinator source code.
#endif


/**@brief Function for initializing the nrf log module.
 */
static void log_init(void)
{
    ret_code_t err_code = NRF_LOG_INIT(NULL);
    APP_ERROR_CHECK(err_code);

    NRF_LOG_DEFAULT_BACKENDS_INIT();
}

/**@brief Function for initializing LEDs.
 */
static void leds_init(void)
{
    bsp_board_init(BSP_INIT_LEDS);
}

/**@brief Callback used in order to visualise network steering period.
 *
 * @param[in]   param   Not used. Required by callback type definition.
 */
static zb_void_t steering_finished(zb_uint8_t param)
{
    UNUSED_PARAMETER(param);
    NRF_LOG_INFO("Network steering finished");
    bsp_board_led_off(ZIGBEE_NETWORK_STATE_LED);
}

/**@brief Retry to form a Zigbee network. */
static zb_void_t bdb_restart_top_level_commissioning(zb_uint8_t param)
{
    UNUSED_RETURN_VALUE(bdb_start_top_level_commissioning(ZB_BDB_NETWORK_STEERING));
}

/**@brief ZigBee stack event handler.
 *
 * @param[in]   param   Reference to ZigBee stack buffer used to pass arguments (signal).
 */
void zboss_signal_handler(zb_uint8_t param)
{
    /* Read signal description out of memory buffer. */
    zb_zdo_app_signal_type_t sig = zb_get_app_signal(param, NULL);
    zb_ret_t                 status = ZB_GET_APP_SIGNAL_STATUS(param);
    zb_ret_t                 zb_err_code;
    zb_bool_t                comm_status;

    switch(sig)
    {
        case ZB_BDB_SIGNAL_DEVICE_FIRST_START: // Device started and commissioned first time after NVRAM erase.
        case ZB_BDB_SIGNAL_DEVICE_REBOOT:      // BDB initialization completed after device reboot, use NVRAM contents during initialization. Device joined/rejoined and started.
            if (status == RET_OK)
            {
                NRF_LOG_INFO("Device started OK. Start network steering.");
                bsp_board_led_on(ZIGBEE_NETWORK_STATE_LED);
                comm_status = bdb_start_top_level_commissioning(ZB_BDB_NETWORK_STEERING);
                ZB_COMM_STATUS_CHECK(comm_status);
            }
            else
            {
                NRF_LOG_ERROR("Device startup failed. Status: %d. Retry network formation after 1 second.", status);
                bsp_board_led_off(ZIGBEE_NETWORK_STATE_LED);
                zb_err_code = ZB_SCHEDULE_ALARM(bdb_restart_top_level_commissioning, 0, ZB_TIME_ONE_SECOND);
                ZB_ERROR_CHECK(zb_err_code);
            }
            break;

        case ZB_BDB_SIGNAL_STEERING:
            if (status == RET_OK)
            {
                /* Schedule an alarm to notify about the end of steering period */
                NRF_LOG_INFO("Network steering started");
                zb_err_code = ZB_SCHEDULE_ALARM(steering_finished, 0, ZB_TIME_ONE_SECOND * ZB_ZGP_DEFAULT_COMMISSIONING_WINDOW);
                ZB_ERROR_CHECK(zb_err_code);
            }
            else
            {
                NRF_LOG_INFO("Network steering failed to start. Status: %d. Retry network formation after 1 second.", status);
                bsp_board_led_off(ZIGBEE_NETWORK_STATE_LED);
                zb_err_code = ZB_SCHEDULE_ALARM(bdb_restart_top_level_commissioning, 0, ZB_TIME_ONE_SECOND);
                ZB_ERROR_CHECK(zb_err_code);
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
            break;
    }

    /* All callbacks should either reuse or free passed buffers. If param == 0, the buffer is invalid (not passed) */
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

    // Initialize.
    log_init();
    leds_init();

    /* Set ZigBee stack logging level and traffic dump subsystem. */
    ZB_SET_TRACE_LEVEL(ZIGBEE_TRACE_LEVEL);
    ZB_SET_TRACE_MASK(ZIGBEE_TRACE_MASK);
    ZB_SET_TRAF_DUMP_OFF();

    /* Initialize ZigBee stack. Pass "zdo_zc" to the stack logging system. */
    ZB_INIT("zdo_zc");

    /* Set device address to the value read from FICR registers. */
    zb_osif_get_ieee_eui64(ieee_addr);
    zb_set_long_address(ieee_addr);

    /* Set channels on which the coordinator will try to create a new network. */
    zb_set_network_coordinator_role(IEEE_CHANNEL_MASK);
    zb_set_max_children(MAX_CHILDREN);

    /* Keep or erase NVRAM to save the network parameters after device reboot or power-off. */
    zb_set_nvram_erase_at_start(ERASE_PERSISTENT_CONFIG);

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
