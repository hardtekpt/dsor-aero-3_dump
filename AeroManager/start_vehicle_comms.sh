#!/bin/bash

###############################################################################
###         Parse Arguments
###############################################################################
if [ "$#" -lt 1 ] || [ "$#" -gt 3 ]; then
  echo "Usage: $0 <hostname> [log|debug] [log|debug]" >&2
  exit 1
fi

if [ "$2" = "log" ] || [ "$3" = "log" ]; then
    LOG='1'
fi

if [ "$2" = "debug" ] || [ "$3" = "debug" ]; then
    DEBUG='1'
fi

###############################################################################
###         Define some things
###############################################################################
HOST="$1"
SUBJECT="$1"

# MavRos system id - Default value
MAVROS_SYS_ID="199"

# OptiTrack computer
OPTITRACK_IP="192.168.1.100"

# UDP MAVLINK COMMS are point-to-point.
# We need two connections, each with a known port (one to receive, one to send)

# Port and IP where to send sensor data (matlab computer) and where to receive
# (listen) for offboard commands (in companion computer).
GCS_IP="192.168.1.240"
GCS_PORT="15999"
RECEIVE_PORT="15999"

# QGC computer (May be the same as the Matlab computer)
QGC_IP="192.168.1.100"
QGC_PORT="14550"

# Change ports as function of the vehicle number
for i in {1..9}
do
    if [ "$1" = "dsor-aero-${i}" ]; then
    ID="${i}"
    GCS_PORT="1500${i}"
    SUBJECT="aero${i}"
    fi
done

# Command for restarting MavLink-Router
KILL_ROUTERD_CMD="killall mavlink-routerd"
START_ROUTERD_CMD="/usr/bin/mavlink-routerd -c ./mavlink-router.conf"
# Change some values for the MavLink-Router configuration (.conf) file
cp mavlink-router.template ./aux
sed "s/TEMPLATE_GCS_PORT/${GCS_PORT}/g" aux > mavlink-router.conf
cp mavlink-router.conf ./aux
sed "s/TEMPLATE_GCS_IP/${GCS_IP}/g" aux > mavlink-router.conf
cp mavlink-router.conf ./aux
sed "s/TEMPLATE_QGC_IP_ADDRESS/${QGC_IP}/g" aux > mavlink-router.conf
cp mavlink-router.conf ./aux
sed "s/TEMPLATE_QGC_PORT/${QGC_PORT}/g" aux > mavlink-router.conf
rm aux


# Check if it is necessary to make logs
if [ -n "$LOG" ]; then
    sed -i '/^#.*Log/s/^#//' mavlink-router.conf
fi

if [ -n "$DEBUG" ]; then
    sed -i '/^#.*ReportStats/s/^#//' mavlink-router.conf
fi


###############################################################################
###         Start tmux session
###############################################################################
#   Initialization adapted from:
#   https://sherif.io/2016/12/29/tmux-workspace-scripts/

# Detach from a tmux session if in one
tmux detach > /dev/null 2>&1

# Don't set up the workspace if there's already a work_${HOST} session running
if tmux list-sessions -F "#{session_name}" | grep -qw "work_${HOST}"; then
    echo "work_${HOST} session already running"

else
    tmux new -s work_${HOST} -d -x "$(tput cols)" -y "$(tput lines)"
    tmux rename-window -t work_${HOST} ros
    #   NOTE: 'tput' is fix from
    #   https://www.reddit.com/r/tmux/comments/7i9dd2/tmux_resizepane_sizes_are_wrong_after_updating_to/

    # Start VRPN to receive mocap data.
    tmux split-window -h -p 66
    tmux split-window -h -p 50
    tmux select-pane -t 0
    COMMAND="roslaunch vrpn_client_ros sample.launch server:=${OPTITRACK_IP}"
    tmux send-keys -t work_${HOST} "${COMMAND}" C-m

    # Send mocap data @ 50 hz to mavlink (original mocap rate is usually 100Hz)
    tmux split-window -v -p 70
    tmux send-keys -t work_${HOST} "sleep 4" C-m
    VRPN_TOPIC="/vrpn_client_node/${SUBJECT}/pose"
    MAVROS_TOPIC="/${SUBJECT}/mavros/vision_pose/pose"
    COMMAND="rosrun topic_tools drop ${VRPN_TOPIC} 2 3 ${MAVROS_TOPIC}"
    tmux send-keys -t work_${HOST} "${COMMAND}" C-m

    # Why? TODO: TEST
    tmux split-window -v -p 50
    # tmux split-window -v -p 66
    # tmux split-window -v -p 50

    tmux select-pane -t 2
    tmux send-keys -t work_${HOST} "sleep 5" C-m
    if [ -n "$DEBUG" ]; then
        tmux send-keys -t work_${HOST} "rostopic echo ${MAVROS_TOPIC}" C-m
    else
        tmux send-keys -t work_${HOST} "rostopic echo -n10 ${MAVROS_TOPIC}" C-m
    fi

    # Make some more echos...
    tmux split-window -h -p 50
    tmux send-keys -t work_${HOST} "sleep 5" C-m
    MAVROS_TOPIC="/${SUBJECT}/mavros/local_position/pose"
    if [ -n "$DEBUG" ]; then
        tmux send-keys -t work_${HOST} "rostopic echo ${MAVROS_TOPIC}" C-m
    else
        tmux send-keys -t work_${HOST} "rostopic echo -n10 ${MAVROS_TOPIC}" C-m
    fi

    # Run MAVROS on companion computer
    tmux select-pane -t 4
    tmux send-keys -t work_${HOST} "sleep 3" C-m
    OPTIONS="fcu_url:=udp://localhost:15000@ gcs_url:=udp://@${GCS_IP}:${GCS_PORT} mavros_sys_id:=${ID} mavros_comp_id:=240 tgt_system:=${ID}"
    COMMAND="ROS_NAMESPACE=${SUBJECT} roslaunch mavros px4.launch ${OPTIONS}"
    tmux send-keys -t work_${HOST} "${COMMAND}" C-m

    # NO LONGER NEEDED - DISABLED PERMANENTELY
    # Disable wifi power management (faster wifi latency)
    # tmux select-pane -t 7
    # tmux send-keys -t work_${HOST} "ssh ${USER}@${HOST} -t 'iwconfig wlp1s0 power off' &" C-m

    # Upload desired configuration for mavlink-router
    tmux select-pane -t 5
    tmux send-keys -t work_${HOST} "${KILL_ROUTERD_CMD}" C-m
    tmux send-keys -t work_${HOST} "${START_ROUTERD_CMD} &" C-m

    tmux split-window -v -p 50
    tmux send-keys -t work_${HOST} "sudo ./disable_c_states 1 &" C-m

fi

tmux attach -t "work_${HOST}"
