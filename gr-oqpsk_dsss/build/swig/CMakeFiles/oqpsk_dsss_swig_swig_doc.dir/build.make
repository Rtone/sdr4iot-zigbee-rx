# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.13

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/local/bin/cmake

# The command to remove a file.
RM = /usr/local/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/ousseynou/sdr4iot_phase2/zigbee-dump/gr-oqpsk_dsss

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/ousseynou/sdr4iot_phase2/zigbee-dump/gr-oqpsk_dsss/build

# Utility rule file for oqpsk_dsss_swig_swig_doc.

# Include the progress variables for this target.
include swig/CMakeFiles/oqpsk_dsss_swig_swig_doc.dir/progress.make

swig/CMakeFiles/oqpsk_dsss_swig_swig_doc: swig/oqpsk_dsss_swig_doc.i


swig/oqpsk_dsss_swig_doc.i: swig/oqpsk_dsss_swig_doc_swig_docs/xml/index.xml
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --blue --bold --progress-dir=/home/ousseynou/sdr4iot_phase2/zigbee-dump/gr-oqpsk_dsss/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Generating python docstrings for oqpsk_dsss_swig_doc"
	cd /home/ousseynou/sdr4iot_phase2/zigbee-dump/gr-oqpsk_dsss/docs/doxygen && /usr/bin/python2 -B /home/ousseynou/sdr4iot_phase2/zigbee-dump/gr-oqpsk_dsss/docs/doxygen/swig_doc.py /home/ousseynou/sdr4iot_phase2/zigbee-dump/gr-oqpsk_dsss/build/swig/oqpsk_dsss_swig_doc_swig_docs/xml /home/ousseynou/sdr4iot_phase2/zigbee-dump/gr-oqpsk_dsss/build/swig/oqpsk_dsss_swig_doc.i

swig/oqpsk_dsss_swig_doc_swig_docs/xml/index.xml: swig/_oqpsk_dsss_swig_doc_tag
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --blue --bold --progress-dir=/home/ousseynou/sdr4iot_phase2/zigbee-dump/gr-oqpsk_dsss/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Generating doxygen xml for oqpsk_dsss_swig_doc docs"
	cd /home/ousseynou/sdr4iot_phase2/zigbee-dump/gr-oqpsk_dsss/build/swig && ./_oqpsk_dsss_swig_doc_tag
	cd /home/ousseynou/sdr4iot_phase2/zigbee-dump/gr-oqpsk_dsss/build/swig && /usr/bin/doxygen /home/ousseynou/sdr4iot_phase2/zigbee-dump/gr-oqpsk_dsss/build/swig/oqpsk_dsss_swig_doc_swig_docs/Doxyfile

oqpsk_dsss_swig_swig_doc: swig/CMakeFiles/oqpsk_dsss_swig_swig_doc
oqpsk_dsss_swig_swig_doc: swig/oqpsk_dsss_swig_doc.i
oqpsk_dsss_swig_swig_doc: swig/oqpsk_dsss_swig_doc_swig_docs/xml/index.xml
oqpsk_dsss_swig_swig_doc: swig/CMakeFiles/oqpsk_dsss_swig_swig_doc.dir/build.make

.PHONY : oqpsk_dsss_swig_swig_doc

# Rule to build all files generated by this target.
swig/CMakeFiles/oqpsk_dsss_swig_swig_doc.dir/build: oqpsk_dsss_swig_swig_doc

.PHONY : swig/CMakeFiles/oqpsk_dsss_swig_swig_doc.dir/build

swig/CMakeFiles/oqpsk_dsss_swig_swig_doc.dir/clean:
	cd /home/ousseynou/sdr4iot_phase2/zigbee-dump/gr-oqpsk_dsss/build/swig && $(CMAKE_COMMAND) -P CMakeFiles/oqpsk_dsss_swig_swig_doc.dir/cmake_clean.cmake
.PHONY : swig/CMakeFiles/oqpsk_dsss_swig_swig_doc.dir/clean

swig/CMakeFiles/oqpsk_dsss_swig_swig_doc.dir/depend:
	cd /home/ousseynou/sdr4iot_phase2/zigbee-dump/gr-oqpsk_dsss/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/ousseynou/sdr4iot_phase2/zigbee-dump/gr-oqpsk_dsss /home/ousseynou/sdr4iot_phase2/zigbee-dump/gr-oqpsk_dsss/swig /home/ousseynou/sdr4iot_phase2/zigbee-dump/gr-oqpsk_dsss/build /home/ousseynou/sdr4iot_phase2/zigbee-dump/gr-oqpsk_dsss/build/swig /home/ousseynou/sdr4iot_phase2/zigbee-dump/gr-oqpsk_dsss/build/swig/CMakeFiles/oqpsk_dsss_swig_swig_doc.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : swig/CMakeFiles/oqpsk_dsss_swig_swig_doc.dir/depend

