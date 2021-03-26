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

#include <gnuradio/io_signature.h>
#include "frequency_offset_plateau_impl.h"

namespace gr {
  namespace CFO_estimator{

    frequency_offset_plateau::sptr
    frequency_offset_plateau::make()
    {
      return gnuradio::get_initial_sptr
        (new frequency_offset_plateau_impl());
    }

    /*
     * The private constructor
     */
	static int ios[] = { sizeof(gr_complex), sizeof(float)};
	static std::vector<int> iosig(ios, ios+sizeof(ios)/sizeof(int));    
    frequency_offset_plateau_impl::frequency_offset_plateau_impl()
      : gr::sync_block("frequency_offset_plateau",
              gr::io_signature::makev(1, 2, iosig),
              gr::io_signature::make(1, 1, sizeof(gr_complex))),
		d_freq_comp(0.0,0.0)
    {}

    /*
     * Our virtual destructor.
     */
    frequency_offset_plateau_impl::~frequency_offset_plateau_impl()
    {
    }

    int
    frequency_offset_plateau_impl::work(int noutput_items,
        gr_vector_const_void_star &input_items,
        gr_vector_void_star &output_items)
    {
      
		const gr_complex *complex_in=(const gr_complex *) input_items[0];
		const float *plateau = (const float *) input_items[1];
		gr_complex *exp_freq_out = (gr_complex *) output_items[0];
		for (int i=0; i<noutput_items; i++){
 			if (plateau[i]==1.0){
				d_freq_comp=complex_in[i];
			}
			exp_freq_out[i]=d_freq_comp;
		}
      return noutput_items;
    }

  } /* namespace CFO_estimator */
} /* namespace gr */

