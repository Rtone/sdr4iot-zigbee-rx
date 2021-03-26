#!/usr/bin/python -u


from __future__ import print_function

from grc.gr_zigbee import gr_zigbee as gr_block
from optparse import OptionParser, OptionGroup
from gnuradio.eng_option import eng_option
from datetime import datetime, timedelta
import binascii
from collections import namedtuple
import csv
import urllib2
import os


# Print current Gnu Radio capture settings
def print_settings(gr, opts):
  print('\n Zigbee-dump:  SDR Zigbee packet dumper')
  print('\nCapture settings:')
  #print(' %-22s: %s MHz' % ('Base Frequency', '{:d}'.format(int(gr.get_central_frequency()))))
  print(' %-22s: %s Hz' % ('Sample rate', '{:d}'.format(int(gr.get_samp_rate()))))
  print(' %-22s: %s dB' % ('Squelch threshold', '{:d}'.format(int(gr.get_squelch_threshold()))))
  print('\nZigbee:')
  print(' %-22s: %s' % ('Scanning Channels', '{:s}'.format(opts.current_zigbee_channels.replace(',', ', '))))
  print(' %-22s: %ss' % ('Scanning Window', '{:.2f}'.format(opts.zigbee_scan_window)))
  #print('csv File: ',  '{:s}'.format(gr.get_csv_file()))
  print('\n%-23s: %s\n' % ('PCAP output file', '{:s}'.format(gr.get_pcap_file())))



# Setup Gnu Radio with defined command line arguments
def init_args(gr, opts):
  gr.set_samp_rate(int(opts.sample_rate))
  gr.set_squelch_threshold(int(opts.squelch_threshold))
  gr.set_zigbee_channel(int(opts.scan_channels[0]))
  gr.set_iq_output(opts.iq_output)
  gr.set_pcap_file(opts.pcap_file)
  gr.set_rf_gain(opts.rf_gain)
  gr.set_duration_seconds(opts.duration_seconds)


# Initialize command line arguments
def init_opts(gr):
  parser = OptionParser(option_class=eng_option, usage="%prog: [opts]")

  # Capture
	
  capture = OptionGroup(parser, 'Capture settings')
  capture.add_option("-o", "--pcap_file", type="string", default="zigbee.cap", help="PCAP output file")
  capture.add_option("-m", "--min_buffer_size", type="int", default=65, help="Minimum buffer size [default=%default]")
  capture.add_option("-s", "--sample-rate", type="eng_float", default=gr.samp_rate, help="Sample rate [default=%default]")
  capture.add_option("-t", "--squelch_threshold", type="eng_float", default=gr.squelch_threshold, help="Squelch threshold (simple squelch) [default=%default]")
  capture.add_option('-g', '--rf-gain', type='int', default=gr.rf_gain, help="RF Gain [default=%default]")
  capture.add_option('-l', '--duration_seconds', type='int', default=gr.duration_seconds, help="Capture duration (seconds) [default=%default]")
  
  # Zigbee
  zigbee= OptionGroup(parser, 'Zigbee:')
  zigbee.add_option("-c", "--current_zigbee_channels", type="string", default='16,16', help="Zigbee channels to scan [default=%default]")
  zigbee.add_option("-w", "--zigbee_scan_window", type="eng_float", default=600, help="Zigbee scan window [default=%default]")
  # Misc
  misc = OptionGroup(parser, "Misc")
  misc.add_option('-d', '--debug', action='store_true', help="Activate debug (dump wrong packets)")
  misc.add_option('-i', '--iq-output', type='string', default=gr.iq_output, help="Filename for IQ data [default=%default]")

  parser.add_option_group(capture)
  parser.add_option_group(zigbee)
  parser.add_option_group(misc)
  return parser.parse_args()

if __name__ == '__main__':
  MIN_BUFFER_LEN = 65

  # Get  Gnu Radio default parameters
  gr_class = gr_block()
  #gr_class.start()

  # Initialize command line arguments
  (opts, args) = init_opts(gr_class)

  #Initialize csv file fields for zigbee packets position in IQ data
  csv_file = opts.iq_output.split('.')[0]+'.csv'
  base_csv = os.path.dirname(csv_file)
  if not os.path.exists(base_csv):
  	os.makedirs(base_csv)
  with open(csv_file, 'w') as csvfile:
        fieldnames = ['Time', 'Start_trame', 'End_trame',
                      'Channel_frequency', 'Sample_rate']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        
  #Initialize  the Gnuradio class with zigbee node and csv file
  #gr_class=gr_block(csv_file)
  #gr_class.start()


  # Verify zigbee channels argument
  if ',' not in opts.current_zigbee_channels:
    opts.current_zigbee_channels += ','

  # Prepare zigbee channels argument
  opts.scan_channels = [int(x) for x in opts.current_zigbee_channels.split(',')]

  # Set Gnu Radio opts
  init_args(gr_class, opts)

  # Print capture settings
  print_settings(gr_class, opts)
  current_hop = 1
  hopping_time = datetime.now() + timedelta(seconds=5)

  # Set initial ZigBee channel
  current_zigbee_chan = opts.scan_channels[0]
  gr_class.set_zigbee_channel(current_zigbee_chan)

  print('Capturing on Zigbee channel [ {:d} ] @ {:d} MHz'.format(current_zigbee_chan, int(gr_class.get_freq_channel())))

  gr_class.start()
	
  try:
   while True:
      # Move to the next ZigBee scanning channel
      if datetime.now() >= hopping_time:
        current_zigbee_chan = opts.scan_channels[current_hop % len(opts.scan_channels)]
        gr_class.set_zigbee_channel(current_zigbee_chan)
        hopping_time = datetime.now() + timedelta(seconds=opts.zigbee_scan_window)
        current_hop +=1

	print("Switching to Zigbee channel [ {:d} ] @ {:d} MHz".format(current_zigbee_chan, int(gr_class.get_freq_channel())))
  except KeyboardInterrupt:
    print("Stopping...")
    pass

  gr_class.stop()
  gr_class.wait()
 

