/* -*- c++ -*- */

#define CFO_ESTIMATOR_API

%include "gnuradio.i"			// the common stuff

//load generated python docstrings
%include "CFO_estimator_swig_doc.i"

%{
#include "CFO_estimator/frequency_offset_estimator.h"
#include "CFO_estimator/frequency_offset_plateau.h"
%}


%include "CFO_estimator/frequency_offset_estimator.h"
GR_SWIG_BLOCK_MAGIC2(CFO_estimator, frequency_offset_estimator);
%include "CFO_estimator/frequency_offset_plateau.h"
GR_SWIG_BLOCK_MAGIC2(CFO_estimator, frequency_offset_plateau);
