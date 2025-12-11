#!/bin/bash
# SPDX-FileCopyrightText: 2025 Saito Shinnosuke
# SPDX-License-Identifier: BSD-3-Clause


dir=~
[ "$1" != "" ] && dir="$1"   

cd "$dir/ros2_ws"
colcon build


source "$dir/.bashrc"

timeout 10 ros2 launch mypkg talk_alarm.launch.py > /tmp/mypkg.log || true

if grep -q 'ALERT' /tmp/mypkg.log; then
    
    exit 0
else
    echo 'ALERT not found in log'
    exit 1
fi

