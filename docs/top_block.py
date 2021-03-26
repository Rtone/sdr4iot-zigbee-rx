#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Top Block
# Generated: Sun Jul 26 17:57:53 2020
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
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from math import sin, pi
from optparse import OptionParser
import CFO_estimator
import frequency_offset_plateau
import osmosdr
import sip
import sys
import time
from gnuradio import qtgui


class top_block(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Top Block")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Top Block")
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

        self.settings = Qt.QSettings("GNU Radio", "top_block")

        if StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
            self.restoreGeometry(self.settings.value("geometry").toByteArray())
        else:
            self.restoreGeometry(self.settings.value("geometry", type=QtCore.QByteArray))

        ##################################################
        # Variables
        ##################################################
        self.transition_width = transition_width = 200e3
        self.samp_rate = samp_rate = 5e6
        self.cutoff_freq = cutoff_freq = 1850e3
        self.lowpass_filter = lowpass_filter = firdes.low_pass(1, samp_rate, cutoff_freq, transition_width, firdes.WIN_HAMMING, 6.76)
        self.half_preamble_len = half_preamble_len = 2*2*32*2

        ##################################################
        # Blocks
        ##################################################
        self.qtgui_time_sink_x_0_1_0_0 = qtgui.time_sink_f(
        	10240, #size
        	samp_rate/200, #samp_rate
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
        self.qtgui_time_sink_x_0_1 = qtgui.time_sink_f(
        	10240, #size
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
        	"compensate frequency offset", #name
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
        self.qtgui_freq_sink_x_1 = qtgui.freq_sink_c(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate, #bw
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_freq_sink_x_1.set_update_time(0.10)
        self.qtgui_freq_sink_x_1.set_y_axis(-140, 10)
        self.qtgui_freq_sink_x_1.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_1.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_1.enable_autoscale(False)
        self.qtgui_freq_sink_x_1.enable_grid(False)
        self.qtgui_freq_sink_x_1.set_fft_average(1.0)
        self.qtgui_freq_sink_x_1.enable_axis_labels(True)
        self.qtgui_freq_sink_x_1.enable_control_panel(False)

        if not True:
          self.qtgui_freq_sink_x_1.disable_legend()

        if "complex" == "float" or "complex" == "msg_float":
          self.qtgui_freq_sink_x_1.set_plot_pos_half(not True)

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_1.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_1.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_1.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_1.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_1.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_1_win = sip.wrapinstance(self.qtgui_freq_sink_x_1.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_freq_sink_x_1_win)
        self.qtgui_freq_sink_x_0 = qtgui.freq_sink_c(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate, #bw
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_freq_sink_x_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0.set_y_axis(-140, 10)
        self.qtgui_freq_sink_x_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_0.enable_grid(False)
        self.qtgui_freq_sink_x_0.set_fft_average(1.0)
        self.qtgui_freq_sink_x_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0.enable_control_panel(False)

        if not True:
          self.qtgui_freq_sink_x_0.disable_legend()

        if "complex" == "float" or "complex" == "msg_float":
          self.qtgui_freq_sink_x_0.set_plot_pos_half(not True)

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_freq_sink_x_0_win)
        self.osmosdr_source_0 = osmosdr.source( args="numchan=" + str(1) + " " + '' )
        self.osmosdr_source_0.set_sample_rate(samp_rate)
        self.osmosdr_source_0.set_center_freq(2.43e9, 0)
        self.osmosdr_source_0.set_freq_corr(0, 0)
        self.osmosdr_source_0.set_dc_offset_mode(2, 0)
        self.osmosdr_source_0.set_iq_balance_mode(0, 0)
        self.osmosdr_source_0.set_gain_mode(False, 0)
        self.osmosdr_source_0.set_gain(100, 0)
        self.osmosdr_source_0.set_if_gain(20, 0)
        self.osmosdr_source_0.set_bb_gain(20, 0)
        self.osmosdr_source_0.set_antenna('', 0)
        self.osmosdr_source_0.set_bandwidth(0, 0)

        self.frequency_offset_plateau_frequency_offset_plateau_0 = frequency_offset_plateau.frequency_offset_plateau()
        self.blocks_vector_source_x_2 = blocks.vector_source_c(((1+1j), (-1+1j), (1-1j), (-1+1j), (1+1j), (-1-1j), (-1-1j), (1+1j), (-1+1j), (-1+1j), (-1-1j), (1-1j), (-1-1j), (1-1j), (1+1j),(1-1j),(1+1j), (-1+1j), (1-1j), (-1+1j), (1+1j), (-1-1j), (-1-1j), (1+1j), (-1+1j), (-1+1j), (-1-1j), (1-1j), (-1-1j), (1-1j), (1+1j),(1-1j),(1+1j), (-1+1j), (1-1j), (-1+1j), (1+1j), (-1-1j), (-1-1j), (1+1j), (-1+1j), (-1+1j), (-1-1j), (1-1j), (-1-1j), (1-1j), (1+1j),(1-1j),(1+1j), (-1+1j), (1-1j), (-1+1j), (1+1j), (-1-1j), (-1-1j), (1+1j), (-1+1j), (-1+1j), (-1-1j), (1-1j), (-1-1j), (1-1j), (1+1j),(1-1j),(1+1j), (-1+1j), (1-1j), (-1+1j), (1+1j), (-1-1j), (-1-1j), (1+1j), (-1+1j), (-1+1j), (-1-1j), (1-1j), (-1-1j), (1-1j), (1+1j),(1-1j),(1+1j), (-1+1j), (1-1j), (-1+1j), (1+1j), (-1-1j), (-1-1j), (1+1j), (-1+1j), (-1+1j), (-1-1j), (1-1j), (-1-1j), (1-1j), (1+1j),(1-1j),(1+1j), (-1+1j), (1-1j), (-1+1j), (1+1j), (-1-1j), (-1-1j), (1+1j), (-1+1j), (-1+1j), (-1-1j), (1-1j), (-1-1j), (1-1j), (1+1j),(1-1j),(1+1j), (-1+1j), (1-1j), (-1+1j), (1+1j), (-1-1j), (-1-1j), (1+1j), (-1+1j), (-1+1j), (-1-1j), (1-1j), (-1-1j), (1-1j), (1+1j),(1-1j),(1+1j), (-1+1j), (1-1j), (-1+1j), (1+1j), (-1-1j), (-1-1j), (1+1j), (-1+1j), (-1+1j), (-1-1j), (1-1j), (-1-1j), (1-1j), (1+1j),(1-1j),(1+1j), (-1+1j), (1-1j), (-1+1j), (1+1j), (-1-1j), (-1-1j), (1+1j), (-1+1j), (-1+1j), (-1-1j), (1-1j), (-1-1j), (1-1j), (1+1j),(1-1j),(1+1j), (-1+1j), (1-1j), (-1+1j), (1+1j), (-1-1j), (-1-1j), (1+1j), (-1+1j), (-1+1j), (-1-1j), (1-1j), (-1-1j), (1-1j), (1+1j),(1-1j),(1+1j), (-1+1j), (1-1j), (-1+1j), (1+1j), (-1-1j), (-1-1j), (1+1j), (-1+1j), (-1+1j), (-1-1j), (1-1j), (-1-1j), (1-1j), (1+1j),(1-1j),(1+1j), (-1+1j), (1-1j), (-1+1j), (1+1j), (-1-1j), (-1-1j), (1+1j), (-1+1j), (-1+1j), (-1-1j), (1-1j), (-1-1j), (1-1j), (1+1j),(1-1j),(1+1j), (-1+1j), (1-1j), (-1+1j), (1+1j), (-1-1j), (-1-1j), (1+1j), (-1+1j), (-1+1j), (-1-1j), (1-1j), (-1-1j), (1-1j), (1+1j),(1-1j),(1+1j), (-1+1j), (1-1j), (-1+1j), (1+1j), (-1-1j), (-1-1j), (1+1j), (-1+1j), (-1+1j), (-1-1j), (1-1j), (-1-1j), (1-1j), (1+1j),(1-1j),(1+1j), (-1+1j), (1-1j), (-1+1j), (1+1j), (-1-1j), (-1-1j), (1+1j), (-1+1j), (-1+1j), (-1-1j), (1-1j), (-1-1j), (1-1j), (1+1j),(1-1j)), True, 1, [])
        self.blocks_vector_source_x_0 = blocks.vector_source_c([0, sin(pi/4), 1, sin(3*pi/4)], True, 1, [])
        self.blocks_repeat_0_0 = blocks.repeat(gr.sizeof_gr_complex*1, 4)
        self.blocks_plateau_detector_fb_0 = blocks.plateau_detector_fb(20, 0.15)
        self.blocks_null_sink_0_0_1_0 = blocks.null_sink(gr.sizeof_gr_complex*1)
        self.blocks_null_sink_0_0_1 = blocks.null_sink(gr.sizeof_float*1)
        self.blocks_null_sink_0_0_0 = blocks.null_sink(gr.sizeof_float*1)
        self.blocks_null_sink_0_0 = blocks.null_sink(gr.sizeof_float*1)
        self.blocks_multiply_xx_0_1_0 = blocks.multiply_vcc(1)
        self.blocks_multiply_xx_0_1 = blocks.multiply_vcc(1)
        self.blocks_float_to_complex_0_0 = blocks.float_to_complex(1)
        self.blocks_delay_1 = blocks.delay(gr.sizeof_gr_complex*1, half_preamble_len)
        self.blocks_delay_0_0 = blocks.delay(gr.sizeof_float*1, 2)
        self.blocks_complex_to_float_0_0 = blocks.complex_to_float(1)
        self.blocks_char_to_float_0 = blocks.char_to_float(1, 1)
        self.CFO_estimator_frequency_offset_estimator_1 = CFO_estimator.frequency_offset_estimator(half_preamble_len*2)
        self.CFO_estimator_frequency_offset_estimator_0 = CFO_estimator.frequency_offset_estimator(half_preamble_len)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.CFO_estimator_frequency_offset_estimator_0, 1), (self.blocks_null_sink_0_0_1, 0))
        self.connect((self.CFO_estimator_frequency_offset_estimator_0, 0), (self.blocks_null_sink_0_0_1_0, 0))
        self.connect((self.CFO_estimator_frequency_offset_estimator_0, 2), (self.blocks_plateau_detector_fb_0, 0))
        self.connect((self.CFO_estimator_frequency_offset_estimator_0, 2), (self.qtgui_time_sink_x_0_1_0_0, 0))
        self.connect((self.CFO_estimator_frequency_offset_estimator_1, 1), (self.blocks_null_sink_0_0, 0))
        self.connect((self.CFO_estimator_frequency_offset_estimator_1, 2), (self.blocks_null_sink_0_0_0, 0))
        self.connect((self.CFO_estimator_frequency_offset_estimator_1, 0), (self.frequency_offset_plateau_frequency_offset_plateau_0, 0))
        self.connect((self.CFO_estimator_frequency_offset_estimator_1, 1), (self.qtgui_time_sink_x_0_1_0_0, 2))
        self.connect((self.blocks_char_to_float_0, 0), (self.frequency_offset_plateau_frequency_offset_plateau_0, 1))
        self.connect((self.blocks_char_to_float_0, 0), (self.qtgui_time_sink_x_0_1, 0))
        self.connect((self.blocks_char_to_float_0, 0), (self.qtgui_time_sink_x_0_1_0_0, 1))
        self.connect((self.blocks_complex_to_float_0_0, 1), (self.blocks_delay_0_0, 0))
        self.connect((self.blocks_complex_to_float_0_0, 0), (self.blocks_float_to_complex_0_0, 0))
        self.connect((self.blocks_delay_0_0, 0), (self.blocks_float_to_complex_0_0, 1))
        self.connect((self.blocks_delay_1, 0), (self.CFO_estimator_frequency_offset_estimator_0, 1))
        self.connect((self.blocks_delay_1, 0), (self.blocks_multiply_xx_0_1_0, 0))
        self.connect((self.blocks_float_to_complex_0_0, 0), (self.CFO_estimator_frequency_offset_estimator_1, 1))
        self.connect((self.blocks_multiply_xx_0_1, 0), (self.blocks_complex_to_float_0_0, 0))
        self.connect((self.blocks_multiply_xx_0_1_0, 0), (self.qtgui_time_sink_x_0_0_1_0_0, 0))
        self.connect((self.blocks_plateau_detector_fb_0, 0), (self.blocks_char_to_float_0, 0))
        self.connect((self.blocks_repeat_0_0, 0), (self.blocks_multiply_xx_0_1, 1))
        self.connect((self.blocks_vector_source_x_0, 0), (self.blocks_multiply_xx_0_1, 0))
        self.connect((self.blocks_vector_source_x_2, 0), (self.blocks_repeat_0_0, 0))
        self.connect((self.frequency_offset_plateau_frequency_offset_plateau_0, 0), (self.blocks_multiply_xx_0_1_0, 1))
        self.connect((self.frequency_offset_plateau_frequency_offset_plateau_0, 0), (self.qtgui_time_sink_x_0_0_1_0, 0))
        self.connect((self.osmosdr_source_0, 0), (self.CFO_estimator_frequency_offset_estimator_0, 0))
        self.connect((self.osmosdr_source_0, 0), (self.CFO_estimator_frequency_offset_estimator_1, 0))
        self.connect((self.osmosdr_source_0, 0), (self.blocks_delay_1, 0))
        self.connect((self.osmosdr_source_0, 0), (self.qtgui_freq_sink_x_1, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "top_block")
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
        self.qtgui_time_sink_x_0_1_0_0.set_samp_rate(self.samp_rate/200)
        self.qtgui_time_sink_x_0_1.set_samp_rate(self.samp_rate)
        self.qtgui_time_sink_x_0_0_1_0_0.set_samp_rate(self.samp_rate)
        self.qtgui_time_sink_x_0_0_1_0.set_samp_rate(self.samp_rate)
        self.qtgui_freq_sink_x_1.set_frequency_range(0, self.samp_rate)
        self.qtgui_freq_sink_x_0.set_frequency_range(0, self.samp_rate)
        self.osmosdr_source_0.set_sample_rate(self.samp_rate)
        self.set_lowpass_filter(firdes.low_pass(1, self.samp_rate, self.cutoff_freq, self.transition_width, firdes.WIN_HAMMING, 6.76))

    def get_cutoff_freq(self):
        return self.cutoff_freq

    def set_cutoff_freq(self, cutoff_freq):
        self.cutoff_freq = cutoff_freq
        self.set_lowpass_filter(firdes.low_pass(1, self.samp_rate, self.cutoff_freq, self.transition_width, firdes.WIN_HAMMING, 6.76))

    def get_lowpass_filter(self):
        return self.lowpass_filter

    def set_lowpass_filter(self, lowpass_filter):
        self.lowpass_filter = lowpass_filter

    def get_half_preamble_len(self):
        return self.half_preamble_len

    def set_half_preamble_len(self, half_preamble_len):
        self.half_preamble_len = half_preamble_len
        self.blocks_delay_1.set_dly(self.half_preamble_len)


def main(top_block_cls=top_block, options=None):

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
