#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2025 Saito Shinnosuke
# SPDX-License-Identifier: BSD-3-Clause

import launch
from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description() -> LaunchDescription:
    return LaunchDescription([
        Node(
            package='mypkg',
            executable='talker',
            name='talker',
        ),
        Node(
            package='mypkg',
            executable='threshold_alarm',
            name='threshold_alarm',
            parameters=[{'threshold': 10}],
            output='screen',
        ),
    ])
