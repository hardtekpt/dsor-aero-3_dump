# Intel Aero How To

## Summary

- Initial Setup
- Brief explaination of UM repos
- Configure `mavlink-routerd`
- Test communication with QGC
- Test communication with Matlab
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

- Download related repos used at SCORE lab (UM)

	https://bitbucket.org/scorelab/aero_manager/
	
	https://bitbucket.org/scorelab/mavlink_matlab/

- Install tmux

		sudo apt-get install tmux

- Disable any firewalls (especially on Windows) as they might interfere with sending and receiving of UDP packets.


## Brief explaination of UM repos

### Aero Manager

The main entry point is `start_vehicle_comms.sh`. 

This script sets up all comunications with the Aero. 

There are options for IPs and ports for where to send packets and where to listen to. Flags are available for enabling logging and debug mode (more verbose info). This script kills the `mavlink-routerd` running onboard and replaces its configuration file with a new one containing the IP, port, and logging, options provided in the command line.

Lines with references to `ROS`, `vicon`, `vision`, and `camera` can be safely ignored if using only attitude (not position) features of the PX4.

Lines with references to `camera` can be safely ignored if cameras are not required.

### mavlink_matlab

This repo is a bugfix improvement on [simulink_mavlink](https://github.com/aditya00j/simulink_mavlink).

It is set up to generate a simulink block that reads `MAVlink` UDP packets and outputs parsed `MAVlink` messages as simulink buses. It also generates simulink blocks that receive `MAVlink` messages as a bus and output packet bytes ready to be sent using UDP blocks.

* To generate the bus objects and blocks (one time only procedure that takes a few minutes) 

	- Run `score/create_sfunctions.m`

* To the bus objects and blocks 
	
	- Run `score/setup_mavlink.m` to load the bus objects and define the appropriate sample times.

	- Run `mavlink_read_useful_sensors_vicon_nonblocking.slx` for a sample application of reading MAVlink messages.

	- Run `mavlink_read_write_with_rpi_command.slx` for an example of _sending_ MAVlink packets

IP and ports for the communication blocks might need to be adjusted. 

#### Important note regading multiple vehicles

The block receiving MAVlink packets does not distinguish between emiting SYS_IDs. At the moment is is not possible to tell which vehicle emited which packet.
*Different quadrotors should send data to different ports.* Doing otherwise will results in mixed data.



## Configure `mavlink-routerd`


On the Intel Aero computer modify `/etc/mavlink-router/main.conf` and 

Comment out the line below to disable logging (it takes up too much space too quickly):
	
	[General]
	#Log=/var/log/mavlink-router

Add other computer endpoints that need to receive MAVLink messages. This will send MAVlink messages as UDP packets to the specified IP and port. Default port is 14550. `name` can be any name. Typical use include sending data to QGC (default port to allow automatic connection) and to Matlab (non-default port is controling multiple quadrotors).

	[UdpEndpoint name]
	Mode = Normal
	Address = 192.168.20.xxx
	# Port = 12345

Alternatively add a broadcast address (could be troublesome if there are too many wifi connections)

	[UdpEndpoint name]
	Mode = Normal
	Address = 192.168.20.255

To set up a port to _receive_ MAVlink packets (for offboard mode) use `Mode = eavesdropping` as in the following example. `Address = 0.0.0.0` allows to receive packets at any interface/IP.

	[UdpEndpoint name]
	Address = 0.0.0.0
	Port = 15000
	Mode = eavesdropping


### Logging CAVEAT

Mavlink-router before Sep 17 2018 only logs data if `SYS_ID = 1`!

`SYS_ID` will differ from quad to quad as it is the only way to distinguish them when using the same communication channels.

To compile from source: (from https://github.com/intel/mavlink-router)

	git clone https://github.com/intel/mavlink-router.git
	git submodule update --init --recursive
	./autogen.sh && ./configure CFLAGS='-g -O2' \
        --sysconfdir=/etc --localstatedir=/var --libdir=/usr/lib64 \
    --prefix=/usr
    make

 Then upload `mavlink-routerd` to all the vehicles.

	scp mavlink-router root@aero1:/usr/bin/ 

More info in https://dev.px4.io/en/log/logging.html , last paragraph of https://404warehouse.net/2018/08/25/using-mavlink-router-to-route-mavlink-streams/

Select logging topics by changing PX4 parameter `SDLOG_PROFILE`. The default of 3 (default topics + EKF2) is too fast for the Aero data link (921k baud).



## Test communication with QGC

Add the apropriate entry to `/etc/mavlink-router/main.conf` and test if the computer at `Address` can connect to the Intel Aero.

	[UdpEndpoint QGC]
	Mode = Normal
	Address = 192.168.xxx.yyy

## Test communication with Matlab

### Receiving packets

Add the apropriate entry to `/etc/mavlink-router/main.conf` and test if the computer at `Address` can receive data in Matlab/Simulink using the provided example simulinks in the `mavlink_matlab` repo. If both QGC and Matlab entries are present then the vehicle can communicate with both simultaneously. Sample code:

	[UdpEndpoint Matlab]
	Mode = Normal
	Port = 12345
	Address = 192.168.xxx.yyy


### Sending packets

Add the apropriate entry to `/etc/mavlink-router/main.conf` and test if the computer at `Address` can receive data in Matlab/Simulink using the provided example simulinks in the `mavlink_matlab` repo. This should not interfere with neither QGC nor the receiving blocks in Matlab. Use QGC to see if packets are being received by the vehicle. Sample code:

	[UdpEndpoint offboard]
	Mode = eavesdropping
	Port = 12345
	Address = 0.0.0.0


### Test offboard mode (attitude)

Receive input from a joystick / gamepad and send attitude commands to the vehicle using the ATTITUDE_TARGET messages. Test first with thrust and angular commands only (not rates). 

**REMOVE PROPELLERS BEFORE INITIAL TESTs!!!**

The motors should not move if not armed but it is better to be safe and remove the propellers before testing any offboard code.

**NOTE: There should be examples of offboard mode in the `mavlink_matlab` repository. MUST verify the option flags before using as some might be incorrect**

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

