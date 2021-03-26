/*
 * Copyright (C) 2013 Bastian Bloessl <bloessl@ccs-labs.org>
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
#ifndef INCLUDED_GR_OQPSK_DSSS_PACKET_SINK_H
#define INCLUDED_GR_OQPSK_DSSS_PACKET_SINK_H

#include <oqpsk_dsss/api.h>
#include <gnuradio/block.h>

namespace gr {
namespace oqpsk_dsss {

class OQPSK_DSSS_API packet_sink : virtual public block
{
public:

	typedef boost::shared_ptr<packet_sink> sptr;
	static sptr make(unsigned int threshold = 10,unsigned int dsss_mode=32,int verbose=0,int verbose2=0,char *filenameRecorder="packet_info.csv",  float channel_frequency = 2.405e9, float sample_rate = 4e6);

};

}  // namespace oqpsk_dsss
}  // namespace gr

#endif /* INCLUDED_GR_OQPSK_DSSS_PACKET_SINK_H */
