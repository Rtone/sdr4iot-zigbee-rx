# ZigBee Dump IEEE 802.15.4 (2.4Ghz)

This tool will permit to dump ZigBee packets by using a SDR. 
It will permit to scan the 16 different channels of 2.4 Ghz central frequency. The demodulation and decoding are done according to IEEE 802.15.4 which uses OQPSK for Zigbee 2.4 Ghz.


## Install dependencies
```sh
# configure gr-oqpsk 
cd gr-oqpsk
mkdir build
cd build
cmake ../
make
sudo make install
sudo ldconfig

#clone gr-foo for wireshark connector
git clone -b maint-3.7 https://github.com/bastibl/gr-foo.git
cg gr-foo
mkdir build
cd build
cmake ../
make 
sudo make install
sudo ldconfig
```

## Command-line parameters


Usage: zigbee_dump.py: [opts]
```
Options:
  -h, --help            show this help message and exit

  Capture settings:
    
     -o PCAP_FILE, --pcap_file=PCAP_FILE
                        PCAP output file 
     -v CSV_FILE, --csv_file=CSV_FILE
            CSV File name for indexes of zigbee packets & robot positions                 
    -m MIN_BUFFER_SIZE, --min_buffer_size=MIN_BUFFER_SIZE
                        Minimum buffer size [default=65]
    -s SAMPLE_RATE, --sample-rate=SAMPLE_RATE
                        Sample rate [default=4000000.0]
    -t SQUELCH_THRESHOLD, --squelch_threshold=SQUELCH_THRESHOLD
                        Squelch threshold (simple squelch) [default=-70]
                
ZigBee::
    -c CURRENT_BLE_CHANNELS, --current_ble_channels=CURRENT_BLE_CHANNELS
                        BLE channels to scan [default=37,38,39]
    -w BLE_SCAN_WINDOW, --ble_scan_window=BLE_SCAN_WINDOW
                        BLE scan window [default=10.24]
    -r ZIGBEE_NODE, --zigbee_node=ZIGBEE_NODE
                              Zigbee node emitter to be tracked
    
 Misc::
    -i,IQ_FILE,  --iq-output=IQ_FILE
                              Filename for IQ data                

```                              