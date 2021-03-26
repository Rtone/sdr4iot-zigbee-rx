/* -*- c++ -*- */
/* 
 * Copyright 2020 <+YOU OR YOUR COMPANY+>.
 * 
 * This is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 3, or (at your option)
 * any later version.
 * 
 * This software is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 * 
 * You should have received a copy of the GNU General Public License
 * along with this software; see the file COPYING.  If not, write to
 * the Free Software Foundation, Inc., 51 Franklin Street,
 * Boston, MA 02110-1301, USA.
 */

#ifdef HAVE_CONFIG_H
#include "config.h"
#endif
#define PI 3.14159265358979323846264338327950288419716939937510582

#include <gnuradio/io_signature.h>
#include "frequency_offset_estimator_impl.h"
#include <gnuradio/expj.h>
#include <complex>
#include <stdlib.h>
#include <math.h>       /* sqrt */


namespace gr {
  namespace CFO_estimator {
    frequency_offset_estimator::sptr
    frequency_offset_estimator::make(int len)
    {
      return gnuradio::get_initial_sptr
        (new frequency_offset_estimator_impl(len));
    }

    /*
     * The private constructor
     */
    static int ios[] = { sizeof(gr_complex), sizeof(float), sizeof(float)};
    static int ios2[] = { sizeof(gr_complex),sizeof(gr_complex)};
    static std::vector<int> iosig(ios, ios+sizeof(ios)/sizeof(int));
    static std::vector<int> iosig2(ios2, ios2+sizeof(ios2)/sizeof(int));
    frequency_offset_estimator_impl::frequency_offset_estimator_impl(int len)
      : gr::sync_block("frequency_offset_estimator",
              gr::io_signature::make(1, 2,sizeof(gr_complex)),  // 2 complex input items(samples and delayed samples phase)
              gr::io_signature::makev(1, 3,iosig)),
      d_freq_offset(0.0),
      d_len(len),
      d_sum_phase_diff(0.0),
      d_corr(0.0),
      d_corr_comp(0.0,0.0),
      d_norm(0.0,0.0),
      d_corr_value(0.0)
	
    {}

    /*
     * Our virtual destructor.
     */
    frequency_offset_estimator_impl::~frequency_offset_estimator_impl()
    {
    }

    int
    frequency_offset_estimator_impl::work(int noutput_items,
        gr_vector_const_void_star &input_items,
        gr_vector_void_star &output_items)
    {
      const gr_complex *complex_in=(const gr_complex *) input_items[0];
      const gr_complex *delayed_complex_in=(const gr_complex *) input_items[1];
      gr_complex *complex_out = (gr_complex *) output_items[0];
      float *freq_out = (float *) output_items[1];
      float *corr_out= (float *) output_items[2];
      int num_samples = 0;
      gr_complex c_offset; 

      for (int i=0; i<noutput_items; i++){
		
	d_sum_phase_diff += std::arg(complex_in[i]*(std::conj(delayed_complex_in[i]))); // sum of phase differences
	d_norm += complex_in[i]*(std::conj(complex_in[i]));
	d_corr_comp += complex_in[i]*(std::conj(delayed_complex_in[i]));
	num_samples += 1;
	if (num_samples%d_len == 0){
		d_freq_offset = d_sum_phase_diff/(2*PI*d_len);
		d_corr_value = sqrt(std::norm(d_corr_comp)/(std::norm(d_norm)));
		d_sum_phase_diff = 0.0;
		d_corr = 0.0;
		d_norm = 0.0;
		d_corr_comp=gr_expj(0.0);
	}
	freq_out[i] = d_freq_offset;
	c_offset = gr_expj(-2*PI*d_freq_offset);
	complex_out[i] = c_offset;
	corr_out[i] = d_corr_value;
	
      }

      return noutput_items;
    }

  } /* namespace CFO_estimator */
} /* namespace gr */

