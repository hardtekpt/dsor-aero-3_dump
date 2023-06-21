# Intel Aero How To

## Summary

- Initial Setup
- Brief explaination of repos
- Test communication with QGC
- Test offboard mode (attitude)
- Configure MOCAP software
- Configure MAVROS
- Test MOCAP & MAVROS



## Initial setup

- Install Ubuntu

- Install Intel Aero repository

From https://github.com/intel-aero/meta-intel-aero/wiki/90-(References)-OS-user-Installation#intel-aero-repository

- Install ROS Kinetic (Intel Aero has best compatibility with Kinetic but should work also with more recent ones)

Following https://github.com/intel-aero/meta-intel-aero/wiki/05-Autonomous-drone-programming-with-ROS

- Assign an IP to the quadrotor (can be dynamic but static makes your life easier) and decide a SYS_ID (for PX4 routing) 

- Download related repos used at DSOR lab 

- Install tmux

		sudo apt-get install tmux

- Disable any firewalls (especially on Windows) as they might interfere with sending and receiving of UDP packets.


## Brief explaination of UM repos

### Aero Manager

The main entry point is `start_vehicle_comms.sh`, which should be edited in case the GCS and QGC computers change their IPs.

This script sets up all comunications with the Aero. 

There are options for IPs and ports for where to send packets and where to listen to. Flags are available for enabling logging and debug mode (more verbose info). This script kills the `mavlink-routerd` running onboard and replaces its configuration file with a new one containing the IP, port, and logging, options provided in the command line.

Lines with references to `ROS`, `optitrack`, `vision`, and `camera` can be safely ignored if using only attitude (not position) features of the PX4.

Lines with references to `camera` can be safely ignored if cameras are not required.

For instance for Intel Aero 3 the usage should be:
	sudo ./start_vehicle_comms.sh dsor-aero-3

#### Important note regading multiple vehicles

The block receiving MAVlink packets does not distinguish between emiting SYS_IDs. At the moment is is not possible to tell which vehicle emited which packet.
*Different quadrotors should send data to different ports.* Doing otherwise will results in mixed data.


## Test communication with QGC

Add the apropriate entries to `./start_vehicle_comms.sh` and test if the computer at the respective IP Addresses can connect to the Intel Aero.

## Test offboard mode (attitude)

**REMOVE PROPELLERS BEFORE INITIAL TESTs!!!**

The motors should not move if not armed but it is better to be safe and remove the propellers before testing any offboard code.

Arm and disarm the motors using the RC remote or through QGC. Remember to enable logs for the flights.

The Aero is configured by default with a switch selecting one of 3 flight modes: 

- Manual
- Altitude hold
- Position

(more detail in https://github.com/intel-aero/meta-intel-aero/wiki/03-First-flight)

For offboard tests without MOCAP the switch should be changed to 

- Manual
- Stabilized
- Offboard

so `offboard` mode can be disabled instantly in case of need.

### Performance tips

- Disable wifi power management (avoids large `lag` time in Wi-Fi communication)

		sudo iwconfig wlp1s0 power off

Note: This change is not permanent. Look online if in need of a permanent solution.

- Disable CPU power saving modes -- Compile and run the sample C code `disable_c_states.c` with

		sudo ./a.out 1 &

The low power CPU states will be disabled as long as `a.out` is running. Verify with `i7z` (`sudo apt-get install i7z` to install).


### Configure MOCAP software
### Configure MAVROS
### Test MOCAP & MAVROS

