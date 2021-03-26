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

#ifndef INCLUDED_CFO_ESTIMATOR_FREQUENCY_FREQUENCY_OFFSET_PLATEAU_IMPL_H
#define INCLUDED_CFO_ESTIMATOR_FREQUENCY_FREQUENCY_OFFSET_PLATEAU_IMPL_H

#include <CFO_estimator/frequency_offset_plateau.h>
#include <complex>
namespace gr {
  namespace CFO_estimator {

    class frequency_offset_plateau_impl : public frequency_offset_plateau
    {
     private:
      std::complex<float> d_freq_comp;

     public:
      frequency_offset_plateau_impl();
      ~frequency_offset_plateau_impl();

      // Where all the action really happens
      int work(int noutput_items,
         gr_vector_const_void_star &input_items,
         gr_vector_void_star &output_items);
    };

  } // namespace namespace CFO_estimator
} // namespace gr

#endif /* INCLUDED_CFO_ESTIMATOR_FREQUENCY_OFFSET_PLATEAU_IMPL_H */

