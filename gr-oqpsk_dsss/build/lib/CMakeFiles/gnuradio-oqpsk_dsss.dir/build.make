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

# Include any dependencies generated for this target.
include lib/CMakeFiles/gnuradio-oqpsk_dsss.dir/depend.make

# Include the progress variables for this target.
include lib/CMakeFiles/gnuradio-oqpsk_dsss.dir/progress.make

# Include the compile flags for this target's objects.
include lib/CMakeFiles/gnuradio-oqpsk_dsss.dir/flags.make

lib/CMakeFiles/gnuradio-oqpsk_dsss.dir/access_code_prefixer.cc.o: lib/CMakeFiles/gnuradio-oqpsk_dsss.dir/flags.make
lib/CMakeFiles/gnuradio-oqpsk_dsss.dir/access_code_prefixer.cc.o: ../lib/access_code_prefixer.cc
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/ousseynou/sdr4iot_phase2/zigbee-dump/gr-oqpsk_dsss/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object lib/CMakeFiles/gnuradio-oqpsk_dsss.dir/access_code_prefixer.cc.o"
	cd /home/ousseynou/sdr4iot_phase2/zigbee-dump/gr-oqpsk_dsss/build/lib && /usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/gnuradio-oqpsk_dsss.dir/access_code_prefixer.cc.o -c /home/ousseynou/sdr4iot_phase2/zigbee-dump/gr-oqpsk_dsss/lib/access_code_prefixer.cc

lib/CMakeFiles/gnuradio-oqpsk_dsss.dir/access_code_prefixer.cc.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/gnuradio-oqpsk_dsss.dir/access_code_prefixer.cc.i"
	cd /home/ousseynou/sdr4iot_phase2/zigbee-dump/gr-oqpsk_dsss/build/lib && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/ousseynou/sdr4iot_phase2/zigbee-dump/gr-oqpsk_dsss/lib/access_code_prefixer.cc > CMakeFiles/gnuradio-oqpsk_dsss.dir/access_code_prefixer.cc.i

lib/CMakeFiles/gnuradio-oqpsk_dsss.dir/access_code_prefixer.cc.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/gnuradio-oqpsk_dsss.dir/access_code_prefixer.cc.s"
	cd /home/ousseynou/sdr4iot_phase2/zigbee-dump/gr-oqpsk_dsss/build/lib && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/ousseynou/sdr4iot_phase2/zigbee-dump/gr-oqpsk_dsss/lib/access_code_prefixer.cc -o CMakeFiles/gnuradio-oqpsk_dsss.dir/access_code_prefixer.cc.s

lib/CMakeFiles/gnuradio-oqpsk_dsss.dir/packet_sink.cc.o: lib/CMakeFiles/gnuradio-oqpsk_dsss.dir/flags.make
lib/CMakeFiles/gnuradio-oqpsk_dsss.dir/packet_sink.cc.o: ../lib/packet_sink.cc
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/ousseynou/sdr4iot_phase2/zigbee-dump/gr-oqpsk_dsss/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Building CXX object lib/CMakeFiles/gnuradio-oqpsk_dsss.dir/packet_sink.cc.o"
	cd /home/ousseynou/sdr4iot_phase2/zigbee-dump/gr-oqpsk_dsss/build/lib && /usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/gnuradio-oqpsk_dsss.dir/packet_sink.cc.o -c /home/ousseynou/sdr4iot_phase2/zigbee-dump/gr-oqpsk_dsss/lib/packet_sink.cc

lib/CMakeFiles/gnuradio-oqpsk_dsss.dir/packet_sink.cc.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/gnuradio-oqpsk_dsss.dir/packet_sink.cc.i"
	cd /home/ousseynou/sdr4iot_phase2/zigbee-dump/gr-oqpsk_dsss/build/lib && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/ousseynou/sdr4iot_phase2/zigbee-dump/gr-oqpsk_dsss/lib/packet_sink.cc > CMakeFiles/gnuradio-oqpsk_dsss.dir/packet_sink.cc.i

lib/CMakeFiles/gnuradio-oqpsk_dsss.dir/packet_sink.cc.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/gnuradio-oqpsk_dsss.dir/packet_sink.cc.s"
	cd /home/ousseynou/sdr4iot_phase2/zigbee-dump/gr-oqpsk_dsss/build/lib && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/ousseynou/sdr4iot_phase2/zigbee-dump/gr-oqpsk_dsss/lib/packet_sink.cc -o CMakeFiles/gnuradio-oqpsk_dsss.dir/packet_sink.cc.s

# Object files for target gnuradio-oqpsk_dsss
gnuradio__oqpsk_dsss_OBJECTS = \
"CMakeFiles/gnuradio-oqpsk_dsss.dir/access_code_prefixer.cc.o" \
"CMakeFiles/gnuradio-oqpsk_dsss.dir/packet_sink.cc.o"

# External object files for target gnuradio-oqpsk_dsss
gnuradio__oqpsk_dsss_EXTERNAL_OBJECTS =

lib/libgnuradio-oqpsk_dsss.so: lib/CMakeFiles/gnuradio-oqpsk_dsss.dir/access_code_prefixer.cc.o
lib/libgnuradio-oqpsk_dsss.so: lib/CMakeFiles/gnuradio-oqpsk_dsss.dir/packet_sink.cc.o
lib/libgnuradio-oqpsk_dsss.so: lib/CMakeFiles/gnuradio-oqpsk_dsss.dir/build.make
lib/libgnuradio-oqpsk_dsss.so: /usr/lib/x86_64-linux-gnu/libboost_filesystem.so
lib/libgnuradio-oqpsk_dsss.so: /usr/lib/x86_64-linux-gnu/libboost_system.so
lib/libgnuradio-oqpsk_dsss.so: /usr/lib/x86_64-linux-gnu/libboost_thread.so
lib/libgnuradio-oqpsk_dsss.so: /usr/lib/x86_64-linux-gnu/libboost_chrono.so
lib/libgnuradio-oqpsk_dsss.so: /usr/lib/x86_64-linux-gnu/libboost_date_time.so
lib/libgnuradio-oqpsk_dsss.so: /usr/lib/x86_64-linux-gnu/libboost_atomic.so
lib/libgnuradio-oqpsk_dsss.so: /usr/lib/x86_64-linux-gnu/libgnuradio-runtime.so
lib/libgnuradio-oqpsk_dsss.so: /usr/lib/x86_64-linux-gnu/libgnuradio-pmt.so
lib/libgnuradio-oqpsk_dsss.so: /usr/lib/x86_64-linux-gnu/liblog4cpp.so
lib/libgnuradio-oqpsk_dsss.so: /usr/lib/x86_64-linux-gnu/libgnuradio-blocks.so
lib/libgnuradio-oqpsk_dsss.so: /usr/lib/x86_64-linux-gnu/libvolk.so
lib/libgnuradio-oqpsk_dsss.so: lib/CMakeFiles/gnuradio-oqpsk_dsss.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/ousseynou/sdr4iot_phase2/zigbee-dump/gr-oqpsk_dsss/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_3) "Linking CXX shared library libgnuradio-oqpsk_dsss.so"
	cd /home/ousseynou/sdr4iot_phase2/zigbee-dump/gr-oqpsk_dsss/build/lib && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/gnuradio-oqpsk_dsss.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
lib/CMakeFiles/gnuradio-oqpsk_dsss.dir/build: lib/libgnuradio-oqpsk_dsss.so

.PHONY : lib/CMakeFiles/gnuradio-oqpsk_dsss.dir/build

lib/CMakeFiles/gnuradio-oqpsk_dsss.dir/clean:
	cd /home/ousseynou/sdr4iot_phase2/zigbee-dump/gr-oqpsk_dsss/build/lib && $(CMAKE_COMMAND) -P CMakeFiles/gnuradio-oqpsk_dsss.dir/cmake_clean.cmake
.PHONY : lib/CMakeFiles/gnuradio-oqpsk_dsss.dir/clean

lib/CMakeFiles/gnuradio-oqpsk_dsss.dir/depend:
	cd /home/ousseynou/sdr4iot_phase2/zigbee-dump/gr-oqpsk_dsss/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/ousseynou/sdr4iot_phase2/zigbee-dump/gr-oqpsk_dsss /home/ousseynou/sdr4iot_phase2/zigbee-dump/gr-oqpsk_dsss/lib /home/ousseynou/sdr4iot_phase2/zigbee-dump/gr-oqpsk_dsss/build /home/ousseynou/sdr4iot_phase2/zigbee-dump/gr-oqpsk_dsss/build/lib /home/ousseynou/sdr4iot_phase2/zigbee-dump/gr-oqpsk_dsss/build/lib/CMakeFiles/gnuradio-oqpsk_dsss.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : lib/CMakeFiles/gnuradio-oqpsk_dsss.dir/depend

