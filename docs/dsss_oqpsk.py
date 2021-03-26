#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: dsss_oqpsk
# Author: ruofan liang
# Generated: Sun Jul 26 18:07:22 2020
##################################################

from distutils.version import StrictVersion

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

from PyQt5 import Qt
from PyQt5 import Qt, QtCore
from gnuradio import analog
from gnuradio import blocks
from gnuradio import channels
from gnuradio import digital
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from math import sin, pi
from optparse import OptionParser
import CFO_estimator
import foo
import frequency_offset_plateau
import ieee802_15_4
import math
import numpy
import oqpsk_dsss
import pmt
import sip
import sys
from gnuradio import qtgui


class dsss_oqpsk(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "dsss_oqpsk")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("dsss_oqpsk")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "dsss_oqpsk")

        if StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
            self.restoreGeometry(self.settings.value("geometry").toByteArray())
        else:
            self.restoreGeometry(self.settings.value("geometry", type=QtCore.QByteArray))

        ##################################################
        # Variables
        ##################################################
        self.transition_width = transition_width = 200e3
        self.samp_rate = samp_rate = 4000000
        self.preamble_samples_to_correlate = preamble_samples_to_correlate = [(1+1j), (-1+1j), (1-1j), (-1+1j), (1+1j), (-1-1j), (-1-1j), (1+1j), (-1+1j), (-1+1j), (-1-1j), (1-1j), (-1-1j), (1-1j), (1+1j),(1-1j)]
        self.cutoff_freq = cutoff_freq = 1850e3
        self.variable_0 = variable_0 = len(preamble_samples_to_correlate)
        self.lowpass_filter = lowpass_filter = firdes.low_pass(1, samp_rate, cutoff_freq, transition_width, firdes.WIN_HAMMING, 6.76)
        self.half_preamble_len = half_preamble_len = 2*2*32*2
        self.dsss_4_8 = dsss_4_8 = [(1+1j), (-1+1j), (1-1j), (-1+1j), (1-1j), (-1-1j), (1+1j), (-1-1j), (-1+1j), (-1+1j), (-1-1j), (1-1j), (-1-1j), (-1-1j), (-1+1j), (1+1j), (-1-1j), (1-1j), (1+1j), (1-1j), (-1+1j), (1+1j), (1-1j), (1+1j), (1+1j), (-1-1j), (-1-1j), (1+1j), (1-1j), (-1+1j), (-1+1j), (1-1j), (1+1j), (1-1j), (1+1j), (-1+1j), (1-1j), (1+1j), (1-1j), (-1-1j), (-1-1j), (1+1j), (-1+1j), (-1+1j), (-1+1j), (1-1j), (-1-1j), (-1-1j), (-1-1j), (1-1j), (-1-1j), (1-1j), (-1+1j), (1+1j), (-1+1j), (1+1j), (1-1j), (-1+1j), (1+1j), (-1-1j), (1+1j), (-1-1j), (1-1j), (-1+1j)]
        self.dsss_4_64 = dsss_4_64 = [(1+1j), (-1+1j), (1-1j), (-1+1j), (1+1j), (-1-1j), (-1-1j), (1+1j), (-1+1j), (-1+1j), (-1-1j), (1-1j), (-1-1j), (1-1j), (1+1j), (1-1j), (1+1j), (-1+1j), (1-1j), (-1+1j), (1+1j), (-1-1j), (-1-1j), (1+1j), (-1+1j), (-1+1j), (-1-1j), (1-1j), (-1-1j), (1-1j), (1+1j), (1-1j), (1-1j), (-1-1j), (1+1j), (-1-1j), (1-1j), (-1+1j), (-1+1j), (1-1j), (-1-1j), (-1-1j), (-1+1j), (1+1j), (-1+1j), (1+1j), (1-1j), (1+1j), (1-1j), (-1-1j), (1+1j), (-1-1j), (1-1j), (-1+1j), (-1+1j), (1-1j), (-1-1j), (-1-1j), (-1+1j), (1+1j), (-1+1j), (1+1j), (1-1j), (1+1j), (-1+1j), (-1+1j), (-1-1j), (1-1j), (-1-1j), (1-1j), (1+1j), (1-1j), (1+1j), (-1+1j), (1-1j), (-1+1j), (1+1j), (-1-1j), (-1-1j), (1+1j), (-1+1j), (-1+1j), (-1-1j), (1-1j), (-1-1j), (1-1j), (1+1j), (1-1j), (1+1j), (-1+1j), (1-1j), (-1+1j), (1+1j), (-1-1j), (-1-1j), (1+1j), (-1-1j), (-1-1j), (-1+1j), (1+1j), (-1+1j), (1+1j), (1-1j), (1+1j), (1-1j), (-1-1j), (1+1j), (-1-1j), (1-1j), (-1+1j), (-1+1j), (1-1j), (-1-1j), (-1-1j), (-1+1j), (1+1j), (-1+1j), (1+1j), (1-1j), (1+1j), (1-1j), (-1-1j), (1+1j), (-1-1j), (1-1j), (-1+1j), (-1+1j), (1-1j), (-1-1j), (1-1j), (1+1j), (1-1j), (1+1j), (-1+1j), (1-1j), (-1+1j), (1+1j), (-1-1j), (-1-1j), (1+1j), (-1+1j), (-1+1j), (-1-1j), (1-1j), (-1-1j), (1-1j), (1+1j), (1-1j), (1+1j), (-1+1j), (1-1j), (-1+1j), (1+1j), (-1-1j), (-1-1j), (1+1j), (-1+1j), (-1+1j), (-1-1j), (1-1j), (-1+1j), (1+1j), (1-1j), (1+1j), (1-1j), (-1-1j), (1+1j), (-1-1j), (1-1j), (-1+1j), (-1+1j), (1-1j), (-1-1j), (-1-1j), (-1+1j), (1+1j), (-1+1j), (1+1j), (1-1j), (1+1j), (1-1j), (-1-1j), (1+1j), (-1-1j), (1-1j), (-1+1j), (-1+1j), (1-1j), (-1-1j), (-1-1j), (-1+1j), (1+1j), (1+1j), (-1-1j), (-1-1j), (1+1j), (-1+1j), (-1+1j), (-1-1j), (1-1j), (-1-1j), (1-1j), (1+1j), (1-1j), (1+1j), (-1+1j), (1-1j), (-1+1j), (1+1j), (-1-1j), (-1-1j), (1+1j), (-1+1j), (-1+1j), (-1-1j), (1-1j), (-1-1j), (1-1j), (1+1j), (1-1j), (1+1j), (-1+1j), (1-1j), (-1+1j), (1-1j), (-1+1j), (-1+1j), (1-1j), (-1-1j), (-1-1j), (-1+1j), (1+1j), (-1+1j), (1+1j), (1-1j), (1+1j), (1-1j), (-1-1j), (1+1j), (-1-1j), (1-1j), (-1+1j), (-1+1j), (1-1j), (-1-1j), (-1-1j), (-1+1j), (1+1j), (-1+1j), (1+1j), (1-1j), (1+1j), (1-1j), (-1-1j), (1+1j), (-1-1j), (1+1j), (1-1j), (1+1j), (-1+1j), (1-1j), (-1+1j), (1+1j), (-1-1j), (-1-1j), (1+1j), (-1+1j), (-1+1j), (-1-1j), (1-1j), (-1-1j), (1-1j), (1+1j), (1-1j), (1+1j), (-1+1j), (1-1j), (-1+1j), (1+1j), (-1-1j), (-1-1j), (1+1j), (-1+1j), (-1+1j), (-1-1j), (1-1j), (-1-1j), (1-1j), (1-1j), (1+1j), (1-1j), (-1-1j), (1+1j), (-1-1j), (1-1j), (-1+1j), (-1+1j), (1-1j), (-1-1j), (-1-1j), (-1+1j), (1+1j), (-1+1j), (1+1j), (1-1j), (1+1j), (1-1j), (-1-1j), (1+1j), (-1-1j), (1-1j), (-1+1j), (-1+1j), (1-1j), (-1-1j), (-1-1j), (-1+1j), (1+1j), (-1+1j), (1+1j), (-1-1j), (1+1j), (-1+1j), (-1+1j), (-1-1j), (1-1j), (-1-1j), (1-1j), (1+1j), (1-1j), (1+1j), (-1+1j), (1-1j), (-1+1j), (1+1j), (-1-1j), (-1-1j), (1+1j), (-1+1j), (-1+1j), (-1-1j), (1-1j), (-1-1j), (1-1j), (1+1j), (1-1j), (1+1j), (-1+1j), (1-1j), (-1+1j), (1+1j), (-1-1j), (-1+1j), (1-1j), (-1-1j), (-1-1j), (-1+1j), (1+1j), (-1+1j), (1+1j), (1-1j), (1+1j), (1-1j), (-1-1j), (1+1j), (-1-1j), (1-1j), (-1+1j), (-1+1j), (1-1j), (-1-1j), (-1-1j), (-1+1j), (1+1j), (-1+1j), (1+1j), (1-1j), (1+1j), (1-1j), (-1-1j), (1+1j), (-1-1j), (1-1j), (-1+1j), (-1-1j), (1-1j), (-1-1j), (1-1j), (1+1j), (1-1j), (1+1j), (-1+1j), (1-1j), (-1+1j), (1+1j), (-1-1j), (-1-1j), (1+1j), (-1+1j), (-1+1j), (-1-1j), (1-1j), (-1-1j), (1-1j), (1+1j), (1-1j), (1+1j), (-1+1j), (1-1j), (-1+1j), (1+1j), (-1-1j), (-1-1j), (1+1j), (-1+1j), (-1+1j), (-1+1j), (1+1j), (-1+1j), (1+1j), (1-1j), (1+1j), (1-1j), (-1-1j), (1+1j), (-1-1j), (1-1j), (-1+1j), (-1+1j), (1-1j), (-1-1j), (-1-1j), (-1+1j), (1+1j), (-1+1j), (1+1j), (1-1j), (1+1j), (1-1j), (-1-1j), (1+1j), (-1-1j), (1-1j), (-1+1j), (-1+1j), (1-1j), (-1-1j), (-1-1j), (1-1j), (-1+1j), (1+1j), (-1-1j), (-1-1j), (1+1j), (-1+1j), (-1+1j), (-1-1j), (1-1j), (-1-1j), (1-1j), (1+1j), (1-1j), (1+1j), (-1+1j), (1-1j), (-1+1j), (1+1j), (-1-1j), (-1-1j), (1+1j), (-1+1j), (-1+1j), (-1-1j), (1-1j), (-1-1j), (1-1j), (1+1j), (1-1j), (1+1j), (-1+1j), (1+1j), (-1-1j), (1-1j), (-1+1j), (-1+1j), (1-1j), (-1-1j), (-1-1j), (-1+1j), (1+1j), (-1+1j), (1+1j), (1-1j), (1+1j), (1-1j), (-1-1j), (1+1j), (-1-1j), (1-1j), (-1+1j), (-1+1j), (1-1j), (-1-1j), (-1-1j), (-1+1j), (1+1j), (-1+1j), (1+1j), (1-1j), (1+1j), (1-1j), (-1-1j)]
        self.dsss_4_32 = dsss_4_32 = [(1+1j), (-1+1j), (1-1j), (-1+1j), (1+1j), (-1-1j), (-1-1j), (1+1j), (-1+1j), (-1+1j), (-1-1j), (1-1j), (-1-1j), (1-1j), (1+1j), (1-1j), (1-1j), (-1-1j), (1+1j), (-1-1j), (1-1j), (-1+1j), (-1+1j), (1-1j), (-1-1j), (-1-1j), (-1+1j), (1+1j), (-1+1j), (1+1j), (1-1j), (1+1j), (-1+1j), (-1+1j), (-1-1j), (1-1j), (-1-1j), (1-1j), (1+1j), (1-1j), (1+1j), (-1+1j), (1-1j), (-1+1j), (1+1j), (-1-1j), (-1-1j), (1+1j), (-1-1j), (-1-1j), (-1+1j), (1+1j), (-1+1j), (1+1j), (1-1j), (1+1j), (1-1j), (-1-1j), (1+1j), (-1-1j), (1-1j), (-1+1j), (-1+1j), (1-1j), (-1-1j), (1-1j), (1+1j), (1-1j), (1+1j), (-1+1j), (1-1j), (-1+1j), (1+1j), (-1-1j), (-1-1j), (1+1j), (-1+1j), (-1+1j), (-1-1j), (1-1j), (-1+1j), (1+1j), (1-1j), (1+1j), (1-1j), (-1-1j), (1+1j), (-1-1j), (1-1j), (-1+1j), (-1+1j), (1-1j), (-1-1j), (-1-1j), (-1+1j), (1+1j), (1+1j), (-1-1j), (-1-1j), (1+1j), (-1+1j), (-1+1j), (-1-1j), (1-1j), (-1-1j), (1-1j), (1+1j), (1-1j), (1+1j), (-1+1j), (1-1j), (-1+1j), (1-1j), (-1+1j), (-1+1j), (1-1j), (-1-1j), (-1-1j), (-1+1j), (1+1j), (-1+1j), (1+1j), (1-1j), (1+1j), (1-1j), (-1-1j), (1+1j), (-1-1j), (1+1j), (1-1j), (1+1j), (-1+1j), (1-1j), (-1+1j), (1+1j), (-1-1j), (-1-1j), (1+1j), (-1+1j), (-1+1j), (-1-1j), (1-1j), (-1-1j), (1-1j), (1-1j), (1+1j), (1-1j), (-1-1j), (1+1j), (-1-1j), (1-1j), (-1+1j), (-1+1j), (1-1j), (-1-1j), (-1-1j), (-1+1j), (1+1j), (-1+1j), (1+1j), (-1-1j), (1+1j), (-1+1j), (-1+1j), (-1-1j), (1-1j), (-1-1j), (1-1j), (1+1j), (1-1j), (1+1j), (-1+1j), (1-1j), (-1+1j), (1+1j), (-1-1j), (-1+1j), (1-1j), (-1-1j), (-1-1j), (-1+1j), (1+1j), (-1+1j), (1+1j), (1-1j), (1+1j), (1-1j), (-1-1j), (1+1j), (-1-1j), (1-1j), (-1+1j), (-1-1j), (1-1j), (-1-1j), (1-1j), (1+1j), (1-1j), (1+1j), (-1+1j), (1-1j), (-1+1j), (1+1j), (-1-1j), (-1-1j), (1+1j), (-1+1j), (-1+1j), (-1+1j), (1+1j), (-1+1j), (1+1j), (1-1j), (1+1j), (1-1j), (-1-1j), (1+1j), (-1-1j), (1-1j), (-1+1j), (-1+1j), (1-1j), (-1-1j), (-1-1j), (1-1j), (-1+1j), (1+1j), (-1-1j), (-1-1j), (1+1j), (-1+1j), (-1+1j), (-1-1j), (1-1j), (-1-1j), (1-1j), (1+1j), (1-1j), (1+1j), (-1+1j), (1+1j), (-1-1j), (1-1j), (-1+1j), (-1+1j), (1-1j), (-1-1j), (-1-1j), (-1+1j), (1+1j), (-1+1j), (1+1j), (1-1j), (1+1j), (1-1j), (-1-1j)]
        self.dsss_4_16 = dsss_4_16 = [(-1-1j), (1+1j), (1+1j), (1-1j), (-1-1j), (1-1j), (-1+1j), (-1+1j), (-1+1j), (1-1j), (1-1j), (1+1j), (-1+1j), (1+1j), (-1-1j), (-1-1j), (-1-1j), (1-1j), (-1+1j), (-1+1j), (-1-1j), (1+1j), (1+1j), (1-1j), (-1+1j), (1+1j), (-1-1j), (-1-1j), (-1+1j), (1-1j), (1-1j), (1+1j), (-1+1j), (-1+1j), (-1-1j), (1+1j), (1+1j), (1-1j), (-1-1j), (1-1j), (-1-1j), (-1-1j), (-1+1j), (1-1j), (1-1j), (1+1j), (-1+1j), (1+1j), (1+1j), (1-1j), (-1-1j), (1-1j), (-1+1j), (-1+1j), (-1-1j), (1+1j), (1-1j), (1+1j), (-1+1j), (1+1j), (-1-1j), (-1-1j), (-1+1j), (1-1j), (-1+1j), (-1-1j), (1+1j), (1+1j), (1-1j), (-1-1j), (1-1j), (-1+1j), (-1-1j), (-1+1j), (1-1j), (1-1j), (1+1j), (-1+1j), (1+1j), (-1-1j), (1-1j), (-1-1j), (1-1j), (-1+1j), (-1+1j), (-1-1j), (1+1j), (1+1j), (1+1j), (-1+1j), (1+1j), (-1-1j), (-1-1j), (-1+1j), (1-1j), (1-1j), (1-1j), (-1+1j), (-1+1j), (-1-1j), (1+1j), (1+1j), (1-1j), (-1-1j), (1+1j), (-1-1j), (-1-1j), (-1+1j), (1-1j), (1-1j), (1+1j), (-1+1j), (1+1j), (1+1j), (1-1j), (-1-1j), (1-1j), (-1+1j), (-1+1j), (-1-1j), (1-1j), (1-1j), (1+1j), (-1+1j), (1+1j), (-1-1j), (-1-1j), (-1+1j)]

        ##################################################
        # Blocks
        ##################################################
        self.qtgui_time_sink_x_0_1_0_0 = qtgui.time_sink_f(
        	10240, #size
        	samp_rate, #samp_rate
        	"real time correlation coefficient", #name
        	3 #number of inputs
        )
        self.qtgui_time_sink_x_0_1_0_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0_1_0_0.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_0_1_0_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0_1_0_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_0_1_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0_1_0_0.enable_autoscale(False)
        self.qtgui_time_sink_x_0_1_0_0.enable_grid(False)
        self.qtgui_time_sink_x_0_1_0_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0_1_0_0.enable_control_panel(True)
        self.qtgui_time_sink_x_0_1_0_0.enable_stem_plot(False)

        if not True:
          self.qtgui_time_sink_x_0_1_0_0.disable_legend()

        labels = ["Peak Correlation", "Plateau Peak detector", "frequency offset", '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["red", "green", "yellow", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "blue"]
        styles = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
                   -1, -1, -1, -1, -1]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]

        for i in xrange(3):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_0_1_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0_1_0_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0_1_0_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0_1_0_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0_1_0_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0_1_0_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0_1_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_1_0_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0_1_0_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_time_sink_x_0_1_0_0_win)
        self.qtgui_time_sink_x_0_1_0 = qtgui.time_sink_f(
        	1024, #size
        	samp_rate, #samp_rate
        	"frq_offset", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_0_1_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0_1_0.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_0_1_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0_1_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_0_1_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0_1_0.enable_autoscale(False)
        self.qtgui_time_sink_x_0_1_0.enable_grid(False)
        self.qtgui_time_sink_x_0_1_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0_1_0.enable_control_panel(True)
        self.qtgui_time_sink_x_0_1_0.enable_stem_plot(False)

        if not True:
          self.qtgui_time_sink_x_0_1_0.disable_legend()

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "blue"]
        styles = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
                   -1, -1, -1, -1, -1]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]

        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_0_1_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0_1_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0_1_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0_1_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0_1_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0_1_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0_1_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_1_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0_1_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_time_sink_x_0_1_0_win)
        self.qtgui_time_sink_x_0_1 = qtgui.time_sink_f(
        	1024, #size
        	samp_rate, #samp_rate
        	"real time plateau", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_0_1.set_update_time(0.10)
        self.qtgui_time_sink_x_0_1.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_0_1.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0_1.enable_tags(-1, True)
        self.qtgui_time_sink_x_0_1.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0_1.enable_autoscale(False)
        self.qtgui_time_sink_x_0_1.enable_grid(False)
        self.qtgui_time_sink_x_0_1.enable_axis_labels(True)
        self.qtgui_time_sink_x_0_1.enable_control_panel(True)
        self.qtgui_time_sink_x_0_1.enable_stem_plot(False)

        if not True:
          self.qtgui_time_sink_x_0_1.disable_legend()

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "blue"]
        styles = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
                   -1, -1, -1, -1, -1]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]

        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_0_1.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0_1.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0_1.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0_1.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0_1.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0_1.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0_1.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_1_win = sip.wrapinstance(self.qtgui_time_sink_x_0_1.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_time_sink_x_0_1_win)
        self.qtgui_time_sink_x_0_0_1_0_0 = qtgui.time_sink_c(
        	1024, #size
        	samp_rate, #samp_rate
        	"complex frequency offset1", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_0_0_1_0_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0_0_1_0_0.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_0_0_1_0_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0_0_1_0_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_0_0_1_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0_0_1_0_0.enable_autoscale(False)
        self.qtgui_time_sink_x_0_0_1_0_0.enable_grid(False)
        self.qtgui_time_sink_x_0_0_1_0_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0_0_1_0_0.enable_control_panel(True)
        self.qtgui_time_sink_x_0_0_1_0_0.enable_stem_plot(False)

        if not True:
          self.qtgui_time_sink_x_0_0_1_0_0.disable_legend()

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "blue"]
        styles = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
                   -1, -1, -1, -1, -1]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]

        for i in xrange(2):
            if len(labels[i]) == 0:
                if(i % 2 == 0):
                    self.qtgui_time_sink_x_0_0_1_0_0.set_line_label(i, "Re{{Data {0}}}".format(i/2))
                else:
                    self.qtgui_time_sink_x_0_0_1_0_0.set_line_label(i, "Im{{Data {0}}}".format(i/2))
            else:
                self.qtgui_time_sink_x_0_0_1_0_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0_0_1_0_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0_0_1_0_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0_0_1_0_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0_0_1_0_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0_0_1_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_0_1_0_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0_0_1_0_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_time_sink_x_0_0_1_0_0_win)
        self.qtgui_time_sink_x_0_0_1_0 = qtgui.time_sink_c(
        	1024, #size
        	samp_rate, #samp_rate
        	"complex frequency offset", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_0_0_1_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0_0_1_0.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_0_0_1_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0_0_1_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_0_0_1_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0_0_1_0.enable_autoscale(False)
        self.qtgui_time_sink_x_0_0_1_0.enable_grid(False)
        self.qtgui_time_sink_x_0_0_1_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0_0_1_0.enable_control_panel(True)
        self.qtgui_time_sink_x_0_0_1_0.enable_stem_plot(False)

        if not True:
          self.qtgui_time_sink_x_0_0_1_0.disable_legend()

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "blue"]
        styles = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
                   -1, -1, -1, -1, -1]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]

        for i in xrange(2):
            if len(labels[i]) == 0:
                if(i % 2 == 0):
                    self.qtgui_time_sink_x_0_0_1_0.set_line_label(i, "Re{{Data {0}}}".format(i/2))
                else:
                    self.qtgui_time_sink_x_0_0_1_0.set_line_label(i, "Im{{Data {0}}}".format(i/2))
            else:
                self.qtgui_time_sink_x_0_0_1_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0_0_1_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0_0_1_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0_0_1_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0_0_1_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0_0_1_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_0_1_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0_0_1_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_time_sink_x_0_0_1_0_win)
        self.qtgui_time_sink_x_0_0 = qtgui.time_sink_c(
        	1024, #size
        	samp_rate, #samp_rate
        	"Noisy", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_0_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0_0.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_0_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0_0.enable_autoscale(False)
        self.qtgui_time_sink_x_0_0.enable_grid(False)
        self.qtgui_time_sink_x_0_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0_0.enable_control_panel(True)
        self.qtgui_time_sink_x_0_0.enable_stem_plot(False)

        if not True:
          self.qtgui_time_sink_x_0_0.disable_legend()

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "blue"]
        styles = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
                   -1, -1, -1, -1, -1]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]

        for i in xrange(2):
            if len(labels[i]) == 0:
                if(i % 2 == 0):
                    self.qtgui_time_sink_x_0_0.set_line_label(i, "Re{{Data {0}}}".format(i/2))
                else:
                    self.qtgui_time_sink_x_0_0.set_line_label(i, "Im{{Data {0}}}".format(i/2))
            else:
                self.qtgui_time_sink_x_0_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_time_sink_x_0_0_win)
        self.qtgui_time_sink_x_0 = qtgui.time_sink_c(
        	1024, #size
        	samp_rate, #samp_rate
        	"preamble", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0.enable_autoscale(False)
        self.qtgui_time_sink_x_0.enable_grid(False)
        self.qtgui_time_sink_x_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0.enable_control_panel(True)
        self.qtgui_time_sink_x_0.enable_stem_plot(False)

        if not True:
          self.qtgui_time_sink_x_0.disable_legend()

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "blue"]
        styles = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
                   -1, -1, -1, -1, -1]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]

        for i in xrange(2):
            if len(labels[i]) == 0:
                if(i % 2 == 0):
                    self.qtgui_time_sink_x_0.set_line_label(i, "Re{{Data {0}}}".format(i/2))
                else:
                    self.qtgui_time_sink_x_0.set_line_label(i, "Im{{Data {0}}}".format(i/2))
            else:
                self.qtgui_time_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_time_sink_x_0_win)
        self.oqpsk_dsss_packet_sink_1 = oqpsk_dsss.packet_sink(12, 32, 0, 0," ",2.405e9,4e6)
        self.oqpsk_dsss_access_code_prefixer_0 = oqpsk_dsss.access_code_prefixer(0x00,0x000000a7)
        self.ieee802_15_4_rime_stack_0 = ieee802_15_4.rime_stack(([129]), ([131]), ([132]), ([23,42]))
        self.ieee802_15_4_mac_0 = ieee802_15_4.mac(False,0x8841,0,0x1aaa,0xffff,0x3344)
        self.frequency_offset_plateau_frequency_offset_plateau_0 = frequency_offset_plateau.frequency_offset_plateau()
        self.foo_wireshark_connector_0 = foo.wireshark_connector(195, False)
        self.digital_clock_recovery_mm_xx_0 = digital.clock_recovery_mm_ff(2, 0.000225, 0.5, 0.03, 0.0002)
        self.digital_chunks_to_symbols_xx_0 = digital.chunks_to_symbols_bc((dsss_4_32), 16)
        self.digital_burst_shaper_xx_0 = digital.burst_shaper_cc((([])), 0, 4, False, "pdu_length")
        self.channels_cfo_model_0 = channels.cfo_model(
                samp_rate,
                0,
                2e6,
                0
        )
        self.blocks_vector_source_x_2 = blocks.vector_source_c(((1+1j), (-1+1j), (1-1j), (-1+1j), (1+1j), (-1-1j), (-1-1j), (1+1j), (-1+1j), (-1+1j), (-1-1j), (1-1j), (-1-1j), (1-1j), (1+1j),(1-1j),(1+1j), (-1+1j), (1-1j), (-1+1j), (1+1j), (-1-1j), (-1-1j), (1+1j), (-1+1j), (-1+1j), (-1-1j), (1-1j), (-1-1j), (1-1j), (1+1j),(1-1j),(1+1j), (-1+1j), (1-1j), (-1+1j), (1+1j), (-1-1j), (-1-1j), (1+1j), (-1+1j), (-1+1j), (-1-1j), (1-1j), (-1-1j), (1-1j), (1+1j),(1-1j),(1+1j), (-1+1j), (1-1j), (-1+1j), (1+1j), (-1-1j), (-1-1j), (1+1j), (-1+1j), (-1+1j), (-1-1j), (1-1j), (-1-1j), (1-1j), (1+1j),(1-1j),(1+1j), (-1+1j), (1-1j), (-1+1j), (1+1j), (-1-1j), (-1-1j), (1+1j), (-1+1j), (-1+1j), (-1-1j), (1-1j), (-1-1j), (1-1j), (1+1j),(1-1j),(1+1j), (-1+1j), (1-1j), (-1+1j), (1+1j), (-1-1j), (-1-1j), (1+1j), (-1+1j), (-1+1j), (-1-1j), (1-1j), (-1-1j), (1-1j), (1+1j),(1-1j),(1+1j), (-1+1j), (1-1j), (-1+1j), (1+1j), (-1-1j), (-1-1j), (1+1j), (-1+1j), (-1+1j), (-1-1j), (1-1j), (-1-1j), (1-1j), (1+1j),(1-1j),(1+1j), (-1+1j), (1-1j), (-1+1j), (1+1j), (-1-1j), (-1-1j), (1+1j), (-1+1j), (-1+1j), (-1-1j), (1-1j), (-1-1j), (1-1j), (1+1j),(1-1j),(1+1j), (-1+1j), (1-1j), (-1+1j), (1+1j), (-1-1j), (-1-1j), (1+1j), (-1+1j), (-1+1j), (-1-1j), (1-1j), (-1-1j), (1-1j), (1+1j),(1-1j),(1+1j), (-1+1j), (1-1j), (-1+1j), (1+1j), (-1-1j), (-1-1j), (1+1j), (-1+1j), (-1+1j), (-1-1j), (1-1j), (-1-1j), (1-1j), (1+1j),(1-1j),(1+1j), (-1+1j), (1-1j), (-1+1j), (1+1j), (-1-1j), (-1-1j), (1+1j), (-1+1j), (-1+1j), (-1-1j), (1-1j), (-1-1j), (1-1j), (1+1j),(1-1j),(1+1j), (-1+1j), (1-1j), (-1+1j), (1+1j), (-1-1j), (-1-1j), (1+1j), (-1+1j), (-1+1j), (-1-1j), (1-1j), (-1-1j), (1-1j), (1+1j),(1-1j),(1+1j), (-1+1j), (1-1j), (-1+1j), (1+1j), (-1-1j), (-1-1j), (1+1j), (-1+1j), (-1+1j), (-1-1j), (1-1j), (-1-1j), (1-1j), (1+1j),(1-1j),(1+1j), (-1+1j), (1-1j), (-1+1j), (1+1j), (-1-1j), (-1-1j), (1+1j), (-1+1j), (-1+1j), (-1-1j), (1-1j), (-1-1j), (1-1j), (1+1j),(1-1j),(1+1j), (-1+1j), (1-1j), (-1+1j), (1+1j), (-1-1j), (-1-1j), (1+1j), (-1+1j), (-1+1j), (-1-1j), (1-1j), (-1-1j), (1-1j), (1+1j),(1-1j),(1+1j), (-1+1j), (1-1j), (-1+1j), (1+1j), (-1-1j), (-1-1j), (1+1j), (-1+1j), (-1+1j), (-1-1j), (1-1j), (-1-1j), (1-1j), (1+1j),(1-1j)), True, 1, [])
        self.blocks_vector_source_x_0 = blocks.vector_source_c([0, sin(pi/4), 1, sin(3*pi/4)], True, 1, [])
        self.blocks_tagged_stream_multiply_length_0 = blocks.tagged_stream_multiply_length(gr.sizeof_gr_complex*1, 'pdu_length', 512)
        self.blocks_tag_gate_0 = blocks.tag_gate(gr.sizeof_float * 1, False)
        self.blocks_repeat_0_0 = blocks.repeat(gr.sizeof_gr_complex*1, 4)
        self.blocks_repeat_0 = blocks.repeat(gr.sizeof_gr_complex*1, 4)
        self.blocks_plateau_detector_fb_0 = blocks.plateau_detector_fb(20, 0.9)
        self.blocks_pdu_to_tagged_stream_0_0_0 = blocks.pdu_to_tagged_stream(blocks.byte_t, 'pdu_length')
        self.blocks_packed_to_unpacked_xx_0 = blocks.packed_to_unpacked_bb(4, gr.GR_LSB_FIRST)
        self.blocks_null_sink_0_1 = blocks.null_sink(gr.sizeof_gr_complex*1)
        self.blocks_null_sink_0_0_0 = blocks.null_sink(gr.sizeof_float*1)
        self.blocks_null_sink_0_0 = blocks.null_sink(gr.sizeof_float*1)
        self.blocks_null_sink_0 = blocks.null_sink(gr.sizeof_gr_complex*1)
        self.blocks_multiply_xx_1 = blocks.multiply_vcc(1)
        self.blocks_multiply_xx_0_1 = blocks.multiply_vcc(1)
        self.blocks_multiply_xx_0 = blocks.multiply_vcc(1)
        self.blocks_message_strobe_0 = blocks.message_strobe(pmt.cons(pmt.make_dict(), pmt.pmt_to_python.numpy_to_uvector(numpy.array([ord(c) for c in "Hello world!"], numpy.uint8))), 100)
        self.blocks_message_debug_0 = blocks.message_debug()
        self.blocks_float_to_complex_0_0 = blocks.float_to_complex(1)
        self.blocks_float_to_complex_0 = blocks.float_to_complex(1)
        self.blocks_file_sink_0 = blocks.file_sink(gr.sizeof_char*1, '/home/ousseynou/Zigbeepacket1.cap', False)
        self.blocks_file_sink_0.set_unbuffered(True)
        self.blocks_delay_1 = blocks.delay(gr.sizeof_gr_complex*1, half_preamble_len)
        self.blocks_delay_0_0 = blocks.delay(gr.sizeof_float*1, 2)
        self.blocks_delay_0 = blocks.delay(gr.sizeof_float*1, 2)
        self.blocks_complex_to_float_0_0 = blocks.complex_to_float(1)
        self.blocks_complex_to_float_0 = blocks.complex_to_float(1)
        self.blocks_char_to_float_0 = blocks.char_to_float(1, 1)
        self.analog_quadrature_demod_cf_0 = analog.quadrature_demod_cf(1)
        self.CFO_estimator_frequency_offset_estimator_0_0 = CFO_estimator.frequency_offset_estimator(half_preamble_len*2)
        self.CFO_estimator_frequency_offset_estimator_0 = CFO_estimator.frequency_offset_estimator(half_preamble_len)

        ##################################################
        # Connections
        ##################################################
        self.msg_connect((self.blocks_message_strobe_0, 'strobe'), (self.ieee802_15_4_rime_stack_0, 'bcin'))
        self.msg_connect((self.ieee802_15_4_mac_0, 'app out'), (self.ieee802_15_4_rime_stack_0, 'fromMAC'))
        self.msg_connect((self.ieee802_15_4_mac_0, 'pdu out'), (self.oqpsk_dsss_access_code_prefixer_0, 'in'))
        self.msg_connect((self.ieee802_15_4_rime_stack_0, 'toMAC'), (self.ieee802_15_4_mac_0, 'app in'))
        self.msg_connect((self.oqpsk_dsss_access_code_prefixer_0, 'out'), (self.blocks_pdu_to_tagged_stream_0_0_0, 'pdus'))
        self.msg_connect((self.oqpsk_dsss_packet_sink_1, 'out'), (self.blocks_message_debug_0, 'print'))
        self.msg_connect((self.oqpsk_dsss_packet_sink_1, 'out'), (self.blocks_message_debug_0, 'print_pdu'))
        self.msg_connect((self.oqpsk_dsss_packet_sink_1, 'out'), (self.foo_wireshark_connector_0, 'in'))
        self.connect((self.CFO_estimator_frequency_offset_estimator_0, 0), (self.blocks_null_sink_0, 0))
        self.connect((self.CFO_estimator_frequency_offset_estimator_0, 2), (self.blocks_plateau_detector_fb_0, 0))
        self.connect((self.CFO_estimator_frequency_offset_estimator_0, 0), (self.qtgui_time_sink_x_0_0_1_0_0, 0))
        self.connect((self.CFO_estimator_frequency_offset_estimator_0, 1), (self.qtgui_time_sink_x_0_1_0, 0))
        self.connect((self.CFO_estimator_frequency_offset_estimator_0, 2), (self.qtgui_time_sink_x_0_1_0_0, 0))
        self.connect((self.CFO_estimator_frequency_offset_estimator_0, 1), (self.qtgui_time_sink_x_0_1_0_0, 2))
        self.connect((self.CFO_estimator_frequency_offset_estimator_0_0, 1), (self.blocks_null_sink_0_0, 0))
        self.connect((self.CFO_estimator_frequency_offset_estimator_0_0, 2), (self.blocks_null_sink_0_0_0, 0))
        self.connect((self.CFO_estimator_frequency_offset_estimator_0_0, 0), (self.frequency_offset_plateau_frequency_offset_plateau_0, 0))
        self.connect((self.analog_quadrature_demod_cf_0, 0), (self.digital_clock_recovery_mm_xx_0, 0))
        self.connect((self.blocks_char_to_float_0, 0), (self.frequency_offset_plateau_frequency_offset_plateau_0, 1))
        self.connect((self.blocks_char_to_float_0, 0), (self.qtgui_time_sink_x_0_1, 0))
        self.connect((self.blocks_char_to_float_0, 0), (self.qtgui_time_sink_x_0_1_0_0, 1))
        self.connect((self.blocks_complex_to_float_0, 1), (self.blocks_delay_0, 0))
        self.connect((self.blocks_complex_to_float_0, 0), (self.blocks_float_to_complex_0, 0))
        self.connect((self.blocks_complex_to_float_0_0, 1), (self.blocks_delay_0_0, 0))
        self.connect((self.blocks_complex_to_float_0_0, 0), (self.blocks_float_to_complex_0_0, 0))
        self.connect((self.blocks_delay_0, 0), (self.blocks_tag_gate_0, 0))
        self.connect((self.blocks_delay_0_0, 0), (self.blocks_float_to_complex_0_0, 1))
        self.connect((self.blocks_delay_1, 0), (self.CFO_estimator_frequency_offset_estimator_0, 1))
        self.connect((self.blocks_delay_1, 0), (self.blocks_multiply_xx_1, 0))
        self.connect((self.blocks_float_to_complex_0, 0), (self.channels_cfo_model_0, 0))
        self.connect((self.blocks_float_to_complex_0_0, 0), (self.CFO_estimator_frequency_offset_estimator_0_0, 1))
        self.connect((self.blocks_multiply_xx_0, 0), (self.blocks_tagged_stream_multiply_length_0, 0))
        self.connect((self.blocks_multiply_xx_0_1, 0), (self.blocks_complex_to_float_0_0, 0))
        self.connect((self.blocks_multiply_xx_0_1, 0), (self.qtgui_time_sink_x_0, 0))
        self.connect((self.blocks_multiply_xx_1, 0), (self.analog_quadrature_demod_cf_0, 0))
        self.connect((self.blocks_multiply_xx_1, 0), (self.blocks_null_sink_0_1, 0))
        self.connect((self.blocks_packed_to_unpacked_xx_0, 0), (self.digital_chunks_to_symbols_xx_0, 0))
        self.connect((self.blocks_pdu_to_tagged_stream_0_0_0, 0), (self.blocks_packed_to_unpacked_xx_0, 0))
        self.connect((self.blocks_plateau_detector_fb_0, 0), (self.blocks_char_to_float_0, 0))
        self.connect((self.blocks_repeat_0, 0), (self.blocks_multiply_xx_0, 1))
        self.connect((self.blocks_repeat_0_0, 0), (self.blocks_multiply_xx_0_1, 1))
        self.connect((self.blocks_tag_gate_0, 0), (self.blocks_float_to_complex_0, 1))
        self.connect((self.blocks_tagged_stream_multiply_length_0, 0), (self.digital_burst_shaper_xx_0, 0))
        self.connect((self.blocks_vector_source_x_0, 0), (self.blocks_multiply_xx_0, 0))
        self.connect((self.blocks_vector_source_x_0, 0), (self.blocks_multiply_xx_0_1, 0))
        self.connect((self.blocks_vector_source_x_2, 0), (self.blocks_repeat_0_0, 0))
        self.connect((self.channels_cfo_model_0, 0), (self.CFO_estimator_frequency_offset_estimator_0, 0))
        self.connect((self.channels_cfo_model_0, 0), (self.CFO_estimator_frequency_offset_estimator_0_0, 0))
        self.connect((self.channels_cfo_model_0, 0), (self.blocks_delay_1, 0))
        self.connect((self.channels_cfo_model_0, 0), (self.qtgui_time_sink_x_0_0, 0))
        self.connect((self.digital_burst_shaper_xx_0, 0), (self.blocks_complex_to_float_0, 0))
        self.connect((self.digital_chunks_to_symbols_xx_0, 0), (self.blocks_repeat_0, 0))
        self.connect((self.digital_clock_recovery_mm_xx_0, 0), (self.oqpsk_dsss_packet_sink_1, 0))
        self.connect((self.foo_wireshark_connector_0, 0), (self.blocks_file_sink_0, 0))
        self.connect((self.frequency_offset_plateau_frequency_offset_plateau_0, 0), (self.blocks_multiply_xx_1, 1))
        self.connect((self.frequency_offset_plateau_frequency_offset_plateau_0, 0), (self.qtgui_time_sink_x_0_0_1_0, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "dsss_oqpsk")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_transition_width(self):
        return self.transition_width

    def set_transition_width(self, transition_width):
        self.transition_width = transition_width
        self.set_lowpass_filter(firdes.low_pass(1, self.samp_rate, self.cutoff_freq, self.transition_width, firdes.WIN_HAMMING, 6.76))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.qtgui_time_sink_x_0_1_0_0.set_samp_rate(self.samp_rate)
        self.qtgui_time_sink_x_0_1_0.set_samp_rate(self.samp_rate)
        self.qtgui_time_sink_x_0_1.set_samp_rate(self.samp_rate)
        self.qtgui_time_sink_x_0_0_1_0_0.set_samp_rate(self.samp_rate)
        self.qtgui_time_sink_x_0_0_1_0.set_samp_rate(self.samp_rate)
        self.qtgui_time_sink_x_0_0.set_samp_rate(self.samp_rate)
        self.qtgui_time_sink_x_0.set_samp_rate(self.samp_rate)
        self.set_lowpass_filter(firdes.low_pass(1, self.samp_rate, self.cutoff_freq, self.transition_width, firdes.WIN_HAMMING, 6.76))
        self.channels_cfo_model_0.set_samp_rate(self.samp_rate)

    def get_preamble_samples_to_correlate(self):
        return self.preamble_samples_to_correlate

    def set_preamble_samples_to_correlate(self, preamble_samples_to_correlate):
        self.preamble_samples_to_correlate = preamble_samples_to_correlate
        self.set_variable_0(len(self.preamble_samples_to_correlate))

    def get_cutoff_freq(self):
        return self.cutoff_freq

    def set_cutoff_freq(self, cutoff_freq):
        self.cutoff_freq = cutoff_freq
        self.set_lowpass_filter(firdes.low_pass(1, self.samp_rate, self.cutoff_freq, self.transition_width, firdes.WIN_HAMMING, 6.76))

    def get_variable_0(self):
        return self.variable_0

    def set_variable_0(self, variable_0):
        self.variable_0 = variable_0

    def get_lowpass_filter(self):
        return self.lowpass_filter

    def set_lowpass_filter(self, lowpass_filter):
        self.lowpass_filter = lowpass_filter

    def get_half_preamble_len(self):
        return self.half_preamble_len

    def set_half_preamble_len(self, half_preamble_len):
        self.half_preamble_len = half_preamble_len
        self.blocks_delay_1.set_dly(self.half_preamble_len)

    def get_dsss_4_8(self):
        return self.dsss_4_8

    def set_dsss_4_8(self, dsss_4_8):
        self.dsss_4_8 = dsss_4_8

    def get_dsss_4_64(self):
        return self.dsss_4_64

    def set_dsss_4_64(self, dsss_4_64):
        self.dsss_4_64 = dsss_4_64

    def get_dsss_4_32(self):
        return self.dsss_4_32

    def set_dsss_4_32(self, dsss_4_32):
        self.dsss_4_32 = dsss_4_32
        self.digital_chunks_to_symbols_xx_0.set_symbol_table((self.dsss_4_32))

    def get_dsss_4_16(self):
        return self.dsss_4_16

    def set_dsss_4_16(self, dsss_4_16):
        self.dsss_4_16 = dsss_4_16


def main(top_block_cls=dsss_oqpsk, options=None):

    if StrictVersion("4.5.0") <= StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.aboutToQuit.connect(quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
