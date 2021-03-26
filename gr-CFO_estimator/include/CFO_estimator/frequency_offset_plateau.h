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


#ifndef INCLUDED_CFO_ESTIMATOR_FREQUENCY_OFFSET_PLATEAU_H
#define INCLUDED_CFO_ESTIMATOR_FREQUENCY_OFFSET_PLATEAU_H

#include <CFO_estimator/api.h>
#include <gnuradio/sync_block.h>

namespace gr {
  namespace CFO_estimator {

    /*!
     * \brief <+description of block+>
     * \ingroup CFO_estimator
     *
     */
    class CFO_ESTIMATOR_API frequency_offset_plateau : virtual public gr::sync_block
    {
     public:
      typedef boost::shared_ptr<frequency_offset_plateau> sptr;

      /*!
       * \brief Return a shared_ptr to a new instance of CFO_estimator::frequency_offset_plateau.
       *
       * To avoid accidental use of raw pointers, CFO_estimator::frequency_offset_plateau's
       * constructor is in a private implementation
       * class. CFO_estimator::frequency_offset_plateau::make is the public interface for
       * creating new instances.
       */
      static sptr make();
    };

  } // namespace CFO_estimator
} // namespace gr

#endif /* INCLUDED_CFO_ESTIMATOR_FREQUENCY_OFFSET_PLATEAU_H */

