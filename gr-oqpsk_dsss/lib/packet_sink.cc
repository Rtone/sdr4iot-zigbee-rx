/*
 * Copyright 2004,2013 Free Software Foundation, Inc.
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 */
#include <oqpsk_dsss/packet_sink.h>
#include <gnuradio/io_signature.h>
#include <cstdio>
#include <errno.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <stdexcept>
#include <cstring>
#include <gnuradio/blocks/count_bits.h>
#include <iostream>
#include <fstream>
#include <bits/stdc++.h> 
#include <stdlib.h> 
#include<string>
#include <chrono> 
#include <ctime> 

using namespace std;
using namespace gr::oqpsk_dsss;
typedef unsigned char uint8_t;
//CRC CCITT, 16 bits little endian
typedef uint16_t crc;

// very d_verbose output for almost each sample
// #define d_verbose 0
// less d_verbose output for higher level debugging
// #define d_verbose2 0

// this is the mapping between chips and symbols if we do
// a fm demodulation of the O-QPSK signal. Note that this
// is different than the O-QPSK chip sequence from the
// 802.15.4 standard since there there is a translation
// happening.
// See "CMOS RFIC Architectures for IEEE 802.15.4 Networks",
// John Notor, Anthony Caviglia, Gary Levy, for more details.
static const unsigned long long CHIP_MAPPING[6][16] = {
          {
			0b1100000,
			0b1001110,
			0b1101100,
			0b1100110,
			0b0101110,
			0b1111010,
			0b1110111,
			0b0000111,
			0b0011111,
			0b0110001,
			0b0010011,
			0b0011001,
			0b1010001,
			0b0000101,
			0b0001000,
			0b1111000
		  },
          {
			0b111010001100010,
			0b011110100011000,
			0b010111101000110,
			0b000101111010001,
			0b110001011110100,
			0b001100010111101,
			0b100011000101111,
			0b101000110001011,
			0b000101110011101,
			0b100001011100111,
			0b101000010111001,
			0b111010000101110,
			0b001110100001011,
			0b110011101000010,
			0b011100111010000,
			0b010111001110100
		  },
          {
		//LSB
			1618456172,//1618456172
			1309113062,//529027475
			1826650030,//778887287
			1724778362,//1368596360
			778887287,//1826650030
			2061946375,//320833617
			2007919840,//2007919840
			125494990,//139563807
			529027475,//1309113062
			838370585,//838370585
			320833617,//2061946375
			422705285,//85537272
			1368596360,//1724778362
			85537272,//422705285
			139563807,//125494990
			2021988657 //2021988657
		},
	{
		//MSB
			1618456172,
			529027475,
			778887287,
			1368596360,
			1826650030,
			320833617,
			2007919840,
			139563807,
			1309113062,
			838370585,
			2061946375,
			85537272,
			1724778362,
			422705285,
			125494990,
			2021988657
	},
        {
			0b110000001110111101011100110110011100000011101111010111001101100,
			0b100111000000111011110101110011011001110000001110111101011100110,
			0b110110011100000011101111010111001101100111000000111011110101110,
			0b110011011001110000001110111101011100110110011100000011101111010,
			0b010111001101100111000000111011110101110011011001110000001110111,
			0b111101011100110110011100000011101111010111001101100111000000111,
			0b111011110101110011011001110000001110111101011100110110011100000,
			0b000011101111010111001101100111000000111011110101110011011001110,
			0b001111110001000010100011001001100011111100010000101000110010011,
			0b011000111111000100001010001100100110001111110001000010100011001,
			0b001001100011111100010000101000110010011000111111000100001010001,
			0b001100100110001111110001000010100011001001100011111100010000101,
			0b101000110010011000111111000100001010001100100110001111110001000,
			0b000010100011001001100011111100010000101000110010011000111111000,
			0b000100001010001100100110001111110001000010100011001001100011111,
			0b111100010000101000110010011000111111000100001010001100100110001
		},
	{
		//chip mapping without translation
			0b11011001110000110101001000101110,
			0b11101101100111000011010100100010,
			0b00101110110110011100001101010010,
			0b00100010111011011001110000110101,
			0b01010010001011101101100111000011,
			0b00110101001000101110110110011100,
			0b11000011010100100010111011011001,
			0b10011100001101010010001011101101,
			0b10001100100101100000011101111011,
			0b10111000110010010110000001110111,
			0b01111011100011001001011000000111,
			0b01110111101110001100100101100000,
			0b00000111011110111000110010010110,
			0b01100000011101111011100011001001,
			0b10010110000001110111101110001100,
			0b11001001011000000111011110111000

	},
    };

static const int MAX_PKT_LEN    = 128 -  1; // remove header and CRC
static const int MAX_LQI_SAMPLES = 8; // Number of chip correlation samples to take
static const int SYNC_HEADER_LEN_CHIPS = 6*2*32; //Number of chips to detect 5 bytes of SYNC header and 1 byte of PHY header 

static const unsigned long long MASKTABLE1[] = {
    0x7E,
    0x7FFE,
    0x7FFFFFFE,
    0x7FFFFFFE,
    0x7FFFFFFFFFFFFFFE,
    0xFFFFFFFE
};

static const unsigned long long MASKTABLE2[] = {
    0xFE,
    0xFFFE,
    0xFFFFFFFE,
    0xFFFFFFFE,
    0xFFFFFFFFFFFFFFFE,
    0xFFFFFFFE
};


class packet_sink_impl : public packet_sink {
public:



//CRC CCITT, 16 bits, POLYNOMIAL(big-endian)=X^16+X^12+X^5+1, POLYNOMIAL(little-endian)=1+X^4+X^11+X^16
//IEEE 802.15.4 uses little endian
uint16_t crc16(unsigned char *buf, int len) {
	uint16_t crc = 0;

	for(int i = 0; i < len; i++) {
		for(int k = 0; k < 8; k++) {
			int input_bit = (!!(buf[i] & (1 << k)) ^ (crc & 1));
			crc = crc >> 1;
			if(input_bit) {
				crc ^= (1 << 15);
				crc ^= (1 << 10);
				crc ^= (1 <<  3);

			}
		}
	}

	return crc;
}


void record_packet_index(char *file,unsigned long start_index_iq_packet,unsigned long end_index_iq_packet,float channel_frequency,float sample_rate)
{
	auto timenow = chrono::system_clock::to_time_t(chrono::system_clock::now());
	timeval curTime;
  	gettimeofday(&curTime, NULL);
  	int milliseconds = curTime.tv_usec/1000;
  	char buffer [80];
  	strftime(buffer, 80, "%Y-%m-%d %H:%M:%S", localtime(&curTime.tv_sec));
  	char currentTime[84] = "";
  	sprintf(currentTime, "%s.%03d", buffer, milliseconds);
	fstream fout;
	fout.open(file,std::fstream::in | std::fstream::out | std::fstream::app);
	fout <<currentTime<<","<< start_index_iq_packet << "," << end_index_iq_packet <<","<< channel_frequency<<","<<sample_rate<<std::endl;
	fout.close();
}

void record_per(float per)
{
	auto timenow = chrono::system_clock::to_time_t(chrono::system_clock::now());
	timeval curTime;
  	gettimeofday(&curTime, NULL);
  	int milliseconds = curTime.tv_usec/1000;
  	char buffer [80];
  	strftime(buffer, 80, "%Y-%m-%d %H:%M:%S", localtime(&curTime.tv_sec));
  	char currentTime[84] = "";
  	sprintf(currentTime, "%s.%03d", buffer, milliseconds);
	fstream fout;
	fout.open("packet_error_rate.csv",std::fstream::in | std::fstream::out | std::fstream::app);
	if (d_dsss_mode==32 && d_dsss_index==2)
	{ 
		fout <<currentTime<<","<< "fsk_demod" << "," << per <<std::endl;
	}
	else if (d_dsss_mode==32 && d_dsss_index==5)
	{
		fout <<currentTime<<","<< "qpsk_demod" << "," << per <<std::endl;
	}
	else
	{
		
	}
	fout.close();
}
void enter_search()
{
	if (d_verbose)
		fprintf(stderr, "@ enter_search\n");

	d_state = STATE_SYNC_SEARCH;
	d_shift_reg = 0;
	d_preamble_cnt = 0;
	d_chip_cnt = 0;
	d_packet_byte = 0;
}
    
void enter_have_sync()
{
	if (d_verbose)
		fprintf(stderr, "@ enter_have_sync\n");

	d_state = STATE_HAVE_SYNC;
	d_packetlen_cnt = 0;
	d_packet_byte = 0;
	d_packet_byte_index = 0;

	// Link Quality Information
	d_lqi = 0;
	d_lqi_sample_count = 0;
}

void enter_have_header(int payload_len)
{
	if (d_verbose)
		fprintf(stderr, "@ enter_have_header (payload_len = %d)\n", payload_len);

	d_state = STATE_HAVE_HEADER;
	d_packetlen  = payload_len;
	d_payload_cnt = 0;
	d_packet_byte = 0;
	d_packet_byte_index = 0;
}


unsigned char decode_chips(unsigned long long chips){
	int i;
	int best_match = 0xFF;
	int min_threshold = d_dsss_mode+1; // Matching to 32 chips, could never have a error of 33 chips

	for(i=0; i<16; i++) {
		// FIXME: we can store the last chip
		// ignore the first and last chip since it depends on the last chip.
		unsigned int threshold = gr::blocks::count_bits64((chips & MASKTABLE2[d_dsss_index]) ^ (CHIP_MAPPING[d_dsss_index][i] & MASKTABLE2[d_dsss_index]));

		if (threshold < min_threshold) {
			best_match = i;
			min_threshold = threshold;
		}
	}

	if (min_threshold < d_threshold) {
		if (d_verbose)
			fprintf(stderr, "Found sequence with %d errors at 0x%x\n", min_threshold, (chips & MASKTABLE2[d_dsss_index]) ^ (CHIP_MAPPING[d_dsss_index][best_match] & MASKTABLE2[d_dsss_index])), fflush(stderr);
		// LQI: Average number of chips correct * MAX_LQI_SAMPLES
		//
		if (d_lqi_sample_count < MAX_LQI_SAMPLES) {
			d_lqi += d_dsss_mode - min_threshold;
			d_lqi_sample_count++;
		}

		return (char)best_match & 0xF;
	}

	return 0xFF;
	
}

int slice(float x) {
	return x > 0 ? 1 : 0;
}

packet_sink_impl(unsigned int threshold,unsigned int dsss_mode,int verbose,int verbose2, char *filenameRecorder, float channel_frequency, float sample_rate)
  : block ("packet_sink",
		   gr::io_signature::make(1, 1, sizeof(float)),
		   gr::io_signature::make(0, 0, 0)),
    d_threshold(threshold),
    d_dsss_mode(dsss_mode),
    d_verbose(verbose),
    d_verbose2(verbose2),
    d_filenameRecorder(filenameRecorder),
    d_channel_frequency(channel_frequency),
    d_sample_rate(sample_rate)

{
	d_sync_vector = 0xA7;

	// Link Quality Information
	d_lqi = 0;
	d_lqi_sample_count = 0;

	switch(d_dsss_mode) {
	    case 8:
	      d_dsss_index = 0;
	      break;
	    case 16:
	      d_dsss_index = 1;
	      break;
	    case 32:
	      d_dsss_index = 2;
	      break;
	    case 64:
	      d_dsss_index = 4;
	      break;
	    default:
	      assert(0);
	      break;
  	}

	if ( d_verbose )
		fprintf(stderr, "syncvec: %x, threshold: %d\n", d_sync_vector, d_threshold),fflush(stderr);
	enter_search();

	message_port_register_out(pmt::mp("out"));

}

~packet_sink_impl()
{
}

int general_work(int noutput, gr_vector_int& ninput_items,
			gr_vector_const_void_star& input_items,
			gr_vector_void_star& output_items ) {

	float *inbuf = (float*)input_items[0];
        int ninput = ninput_items[0];
	int count=0;

	
	if (d_verbose)
		fprintf(stderr,">>> Entering state machine\n"),fflush(stderr);
	
	while(count < ninput) {
        	
		switch(d_state) {

		case STATE_SYNC_SEARCH:    // Look for sync vector
			if (d_verbose)
				fprintf(stderr,"SYNC Search, ninput=%d syncvec=%x\n", ninput, d_sync_vector),fflush(stderr);

			while (count < ninput) {

				if(slice(inbuf[count++]))
					d_shift_reg = (d_shift_reg << 1) | 1;
				else
					d_shift_reg = d_shift_reg << 1;

				if(d_preamble_cnt > 0){
					d_chip_cnt = d_chip_cnt+1;
				}

				// The first if block syncronizes to chip sequences.
				if(d_preamble_cnt == 0){
					unsigned int threshold;
					threshold = gr::blocks::count_bits64((d_shift_reg & MASKTABLE1[d_dsss_index]) ^ (CHIP_MAPPING[d_dsss_index][0] & MASKTABLE1[d_dsss_index]));
					if(threshold < d_threshold) {
						if (d_verbose2)
							fprintf(stderr,"Found 0 in chip sequence\n"),fflush(stderr);
						// we found a 0 in the chip sequence
						d_preamble_cnt+=1;
					}
				} else {
					// we found the first 0, thus we only have to do the calculation every dsss_mode chips
					if(d_chip_cnt == d_dsss_mode){
						d_chip_cnt = 0;

						if(d_packet_byte == 0) {
							if (gr::blocks::count_bits64((d_shift_reg & MASKTABLE1[d_dsss_index]) ^ (CHIP_MAPPING[d_dsss_index][0] & MASKTABLE2[d_dsss_index])) <= d_threshold) {
								if (d_verbose2)
									fprintf(stderr,"Found %d 0 in chip sequence\n", d_preamble_cnt),fflush(stderr);
								// we found an other 0 in the chip sequence
								d_packet_byte = 0;
								d_preamble_cnt ++;
							} else if (gr::blocks::count_bits64((d_shift_reg & MASKTABLE1[d_dsss_index]) ^ (CHIP_MAPPING[d_dsss_index][7] & MASKTABLE2[d_dsss_index])) <= d_threshold) {
								if (d_verbose2)
									fprintf(stderr,"Found first SFD\n"),fflush(stderr);
								d_packet_byte = 7 << 4;
							} else {
								// we are not in the synchronization header
								if (d_verbose2)
									fprintf(stderr, "Wrong first byte of SFD. %llu\n", d_shift_reg), fflush(stderr);
								enter_search();
								break;
							}

						} else {
							if (gr::blocks::count_bits64((d_shift_reg & MASKTABLE1[d_dsss_index]) ^ (CHIP_MAPPING[d_dsss_index][10] & MASKTABLE2[d_dsss_index])) <= d_threshold) {
								d_packet_byte |= 0xA;
								if (d_verbose2)
									fprintf(stderr,"Found sync, 0x%x\n", d_packet_byte),fflush(stderr);
								// found SDF
								// setup for header decode
								enter_have_sync();
								break;
							} else {
								if (d_verbose)
									fprintf(stderr, "Wrong second byte of SFD. %llu\n", d_shift_reg), fflush(stderr);
								enter_search();
								break;
							}
						}
					}
				}
			}
			break;

		case STATE_HAVE_SYNC:
			if (d_verbose2)
				fprintf(stderr,"Header Search bitcnt=%d, header=0x%08x\n", d_headerbitlen_cnt, d_header),
				fflush(stderr);

			while (count < ninput) {		// Decode the bytes one after another.
				if(slice(inbuf[count++]))
					d_shift_reg = (d_shift_reg << 1) | 1;
				else
					d_shift_reg = d_shift_reg << 1;

				d_chip_cnt = d_chip_cnt+1;

				if(d_chip_cnt == d_dsss_mode){
					d_chip_cnt = 0;
					unsigned char c = decode_chips(d_shift_reg);
					if(c == 0xFF){
						// something is wrong. restart the search for a sync
						if(d_verbose2)
							fprintf(stderr, "Found a not valid chip sequence! %llu\n", d_shift_reg), fflush(stderr);

						enter_search();
						break;
					}

					if(d_packet_byte_index == 0){
						d_packet_byte = c;
					} else {
						// c is always < 15
						d_packet_byte |= c << 4;
					}
					d_packet_byte_index = d_packet_byte_index + 1;
					if(d_packet_byte_index%2 == 0){
						// we have a complete byte which represents the frame length.
						int frame_len = d_packet_byte;
						if(frame_len <= MAX_PKT_LEN){
							enter_have_header(frame_len);
						} else {
							enter_search();
						}
						break;
					}
				}
			}
			break;

		case STATE_HAVE_HEADER:
			if (d_verbose2)
				fprintf(stderr,"Packet Build count=%d, ninput=%d, packet_len=%d\n", count, ninput, d_packetlen),fflush(stderr);

			while (count < ninput) {   // shift bits into bytes of packet one at a time
				//printf("count:%d\n",count);
				if(slice(inbuf[count++]))
					d_shift_reg = (d_shift_reg << 1) | 1;
				else
					d_shift_reg = d_shift_reg << 1;
		

				d_chip_cnt = (d_chip_cnt+1)%d_dsss_mode;

				if(d_chip_cnt == 0){
					unsigned char c = decode_chips(d_shift_reg);
					if(c == 0xff){
						// something is wrong. restart the search for a sync
						if(d_verbose2)
							fprintf(stderr, "Found a not valid chip sequence! %llu\n", d_shift_reg), fflush(stderr);

						enter_search();
						break;
					}
					// the first symbol represents the first part of the byte.
					if(d_packet_byte_index == 0){
						d_packet_byte = c;
					} else {
						// c is always < 15
						d_packet_byte |= c << 4;
					}
					d_packet_byte_index = d_packet_byte_index + 1;
					
					if(d_packet_byte_index%2 == 0){
						// we have a complete byte
						if (d_verbose2)
							fprintf(stderr, "packetcnt: %d, payloadcnt: %d, payload 0x%x, d_packet_byte_index: %d\n", d_packetlen_cnt, d_payload_cnt, d_packet_byte, d_packet_byte_index), fflush(stderr);

						d_packet[d_packetlen_cnt++] = d_packet_byte;
						d_payload_cnt++;
						d_packet_byte_index = 0;
						if (d_payload_cnt >= d_packetlen){	// packet is filled, including CRC. might do check later in here
							unsigned int scaled_lqi = (d_lqi / MAX_LQI_SAMPLES) << 3;
							unsigned char lqi = (scaled_lqi >= 256? 255 : scaled_lqi);

							pmt::pmt_t meta = pmt::make_dict();
							meta = pmt::dict_add(meta, pmt::mp("lqi"), pmt::from_long(lqi));

							std::memcpy(buf, d_packet, d_packetlen_cnt);
							pmt::pmt_t payload = pmt::init_u8vector(d_packetlen_cnt, d_packet);
							crc = crc16(d_packet,d_packetlen-2);
							check_crc = (check_crc >> 8)^(crc &0xFF);
							check_crc = (check_crc << 8)^(crc >> 8);
 							crc_packet = (crc_packet >> 8)^(d_packet[d_packetlen-2]& 0xFF);
							crc_packet = (crc_packet << 8)^(d_packet[d_packetlen-1]& 0xFF);
							packet_count++;
							if (packet_count == 50){
								float packet_error_rate= (float)num_packet_errors / (float)packet_count;
								packet_count=0;
								num_packet_errors=0;
								record_per(packet_error_rate);
								printf("Packet error rate: %g\n",packet_error_rate );
							}
							if (gr::blocks::count_bits64((check_crc & 0xFFFF) ^ (crc_packet & 0xFFFF)) != 0) {
									 num_packet_errors++;
							}
							else{
								if(d_packetlen_cnt >= 5){ //Minimum packet size
									printf("Correct crc.\n"); 
									message_port_pub(pmt::mp("out"), pmt::cons(meta, payload));
									end_index_iq_packet=(count+len_buffer_chips)*2;
									start_index_iq_packet=end_index_iq_packet- d_packetlen_cnt*2*d_dsss_mode*2;
									printf("index in IQ data: %ld\n",start_index_iq_packet );
									printf("End packet in IQ data: %ld\n",end_index_iq_packet);
															record_packet_index(d_filenameRecorder,start_index_iq_packet,end_index_iq_packet,d_channel_frequency,
		    d_sample_rate);
								}
							}
								
							if(d_verbose2)
								fprintf(stderr, "Adding message of size %d to queue\n", d_packetlen_cnt);
							enter_search();
							break;
						}
					}
				}
			}
			break;

		default:
			assert(0);
			break;

		}
	}

	if(d_verbose2)
		fprintf(stderr, "Samples Processed: %d\n", ninput_items[0]), fflush(stderr);

        consume(0, ninput_items[0]);
	len_buffer_chips += ninput;
	return 0;
}

private:
	enum {STATE_SYNC_SEARCH, STATE_HAVE_SYNC, STATE_HAVE_HEADER} d_state;

	unsigned int      d_sync_vector;           // 802.15.4 standard is 4x 0 bytes and 1x0xA7
	unsigned int      d_threshold;             // how many bits may be wrong in sync vector

	unsigned long long     d_shift_reg;             // used to look for sync_vector
	int               d_preamble_cnt;          // count on where we are in preamble
	int               d_chip_cnt;              // counts the chips collected

	unsigned int      d_header;                // header bits
	int               d_headerbitlen_cnt;      // how many so far

	uint8_t     	  d_packet[MAX_PKT_LEN];   // assembled payload
	uint8_t     	  d_packet_byte;           // byte being assembled
	int               d_packet_byte_index;     // which bit of d_packet_byte we're working on
	int               d_packetlen;             // length of packet
	int               d_packetlen_cnt;         // how many so far
	int               d_payload_cnt;           // how many bytes in payload

	unsigned int      d_lqi;                   // Link Quality Information
	unsigned int      d_lqi_sample_count;

  	int               d_verbose;                 // very verbose output for almost each sample
  	int               d_verbose2;                // less verbose output for higher level debugging
  	char              *d_filenameRecorder;
  	int  		  d_sample_rate;
	int 		  d_channel_frequency;
  	unsigned int      d_dsss_mode;
  	int               d_dsss_index;
	int 		  num_packet_errors=0;
	uint16_t          crc;
	uint16_t          crc_packet=0;
	uint16_t          check_crc=0;
	unsigned long     len_buffer_chips=0;
	unsigned long     start_index_iq_packet=0;
	unsigned long     end_index_iq_packet=0;
	unsigned long     packet_count=0;
	// FIXME:
	char buf[256];
};

packet_sink::sptr packet_sink::make(unsigned int threshold,unsigned int dsss_mode,int verbose, int verbose2,char *filenameRecorder, float channel_frequency, float sample_rate) {
	return gnuradio::get_initial_sptr(new packet_sink_impl(threshold,dsss_mode,verbose,verbose2,filenameRecorder,channel_frequency,sample_rate));
}
