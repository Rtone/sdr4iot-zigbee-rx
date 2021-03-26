#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Not titled yet
# Author: thibaud
# GNU Radio version: 3.8.1.0

from gnuradio import analog
import math
from gnuradio import blocks
from gnuradio import digital
from gnuradio import filter
from gnuradio import gr
from gnuradio.filter import firdes
import sys
import signal
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
from gnuradio import uhd
import time
import foo
import ieee802_15_4

class gr_zigbee(gr.top_block):

    def __init__(self):
        gr.top_block.__init__(self, "Not titled yet")

        ##################################################
        # Variables
        ##################################################
        self.zigbee_channel = zigbee_channel = 15
        self.samp_rate = samp_rate = 4e6
        self.duration_seconds = duration_seconds = 10
        self.center_freq = center_freq = 2.405e9+5e6*(zigbee_channel-11)
        self.squelch_threshold = squelch_threshold = -70
        self.rf_gain = rf_gain = 10
        self.pcap_file = pcap_file = "zigbee.cap"
        self.num_samples = num_samples = duration_seconds*samp_rate
        self.iq_output = iq_output = "zigbee.sigmf-data"
        self.freq_channel = freq_channel = center_freq

        ##################################################
        # Blocks
        ##################################################
        self.uhd_usrp_source_0 = uhd.usrp_source(
            ",".join(("", "")),
            uhd.stream_args(
                cpu_format="fc32",
                args='',
                channels=list(range(0,1)),
            ),
        )
        self.uhd_usrp_source_0.set_center_freq(center_freq, 0)
        self.uhd_usrp_source_0.set_gain(rf_gain, 0)
        self.uhd_usrp_source_0.set_antenna('J2', 0)
        self.uhd_usrp_source_0.set_samp_rate(samp_rate)
        # No synchronization enforced.
        self.single_pole_iir_filter_xx_0 = filter.single_pole_iir_filter_ff(0.00016, 1)
        self.ieee802_15_4_packet_sink_1 = ieee802_15_4.packet_sink(10)
        self.foo_wireshark_connector_0 = foo.wireshark_connector(195, True)
        self.digital_clock_recovery_mm_xx_0 = digital.clock_recovery_mm_ff(2, 0.000225, 0.5, 0.03, 0.0002)
        self.blocks_sub_xx_0 = blocks.sub_ff(1)
        self.blocks_message_debug_0 = blocks.message_debug()
        self.blocks_head_0 = blocks.head(gr.sizeof_gr_complex*1, int(num_samples))
        self.blocks_file_sink_0_0 = blocks.file_sink(gr.sizeof_char*1, 'zigbee.cap', False)
        self.blocks_file_sink_0_0.set_unbuffered(True)
        self.blocks_file_sink_0 = blocks.file_sink(gr.sizeof_gr_complex*1, iq_output, False)
        self.blocks_file_sink_0.set_unbuffered(False)
        self.analog_quadrature_demod_cf_0 = analog.quadrature_demod_cf(1)



        ##################################################
        # Connections
        ##################################################
        self.msg_connect((self.ieee802_15_4_packet_sink_1, 'out'), (self.blocks_message_debug_0, 'print'))
        self.msg_connect((self.ieee802_15_4_packet_sink_1, 'out'), (self.blocks_message_debug_0, 'print_pdu'))
        self.msg_connect((self.ieee802_15_4_packet_sink_1, 'out'), (self.foo_wireshark_connector_0, 'in'))
        self.connect((self.analog_quadrature_demod_cf_0, 0), (self.blocks_sub_xx_0, 0))
        self.connect((self.analog_quadrature_demod_cf_0, 0), (self.single_pole_iir_filter_xx_0, 0))
        self.connect((self.blocks_head_0, 0), (self.analog_quadrature_demod_cf_0, 0))
        self.connect((self.blocks_head_0, 0), (self.blocks_file_sink_0, 0))
        self.connect((self.blocks_sub_xx_0, 0), (self.digital_clock_recovery_mm_xx_0, 0))
        self.connect((self.digital_clock_recovery_mm_xx_0, 0), (self.ieee802_15_4_packet_sink_1, 0))
        self.connect((self.foo_wireshark_connector_0, 0), (self.blocks_file_sink_0_0, 0))
        self.connect((self.single_pole_iir_filter_xx_0, 0), (self.blocks_sub_xx_0, 1))
        self.connect((self.uhd_usrp_source_0, 0), (self.blocks_head_0, 0))

    def get_zigbee_channel(self):
        return self.zigbee_channel

    def set_zigbee_channel(self, zigbee_channel):
        self.zigbee_channel = zigbee_channel
        self.set_center_freq(2.405e9+5e6*(self.zigbee_channel-11))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.set_num_samples(self.duration_seconds*self.samp_rate)
        self.uhd_usrp_source_0.set_samp_rate(self.samp_rate)

    def get_duration_seconds(self):
        return self.duration_seconds

    def set_duration_seconds(self, duration_seconds):
        self.duration_seconds = duration_seconds
        self.set_num_samples(self.duration_seconds*self.samp_rate)

    def get_center_freq(self):
        return self.center_freq

    def set_center_freq(self, center_freq):
        self.center_freq = center_freq
        self.set_freq_channel(self.center_freq)
        self.uhd_usrp_source_0.set_center_freq(self.center_freq, 0)

    def get_squelch_threshold(self):
        return self.squelch_threshold

    def set_squelch_threshold(self, squelch_threshold):
        self.squelch_threshold = squelch_threshold

    def get_rf_gain(self):
        return self.rf_gain

    def set_rf_gain(self, rf_gain):
        self.rf_gain = rf_gain
        self.uhd_usrp_source_0.set_gain(self.rf_gain, 0)

    def get_pcap_file(self):
        return self.pcap_file

    def set_pcap_file(self, pcap_file):
        self.pcap_file = pcap_file

    def get_num_samples(self):
        return self.num_samples

    def set_num_samples(self, num_samples):
        self.num_samples = num_samples
        self.blocks_head_0.set_length(int(self.num_samples))

    def get_iq_output(self):
        return self.iq_output

    def set_iq_output(self, iq_output):
        self.iq_output = iq_output
        self.blocks_file_sink_0.open(self.iq_output)

    def get_freq_channel(self):
        return self.freq_channel

    def set_freq_channel(self, freq_channel):
        self.freq_channel = freq_channel



def main(top_block_cls=gr_zigbee, options=None):
    tb = top_block_cls()

    def sig_handler(sig=None, frame=None):
        tb.stop()
        tb.wait()
        sys.exit(0)

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    tb.start()
    try:
        input('Press Enter to quit: ')
    except EOFError:
        pass
    tb.stop()
    tb.wait()


if __name__ == '__main__':
    main()
