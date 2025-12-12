#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2025 Saito Shinnosuke
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16, Bool


class ThresholdAlarm(Node):
    def __init__(self):
        super().__init__('threshold_alarm')
        self.declare_parameter('threshold', 10)
        self._threshold = self.get_parameter('threshold').value
        self._over = False  
        self._sub = self.create_subscription(
            Int16,
            'countup',
            self._on_count,
            10,
        )
        self._pub = self.create_publisher(Bool, 'over_threshold', 10)
        self.get_logger().info(
            f'threshold_alarm started (threshold={self._threshold})'
        )

    def _on_count(self, msg: Int16):
        if self._over:
            return

        if msg.data >= self._threshold:
            self._over = True
            self.get_logger().info(
                f'ALERT: value {msg.data} >= threshold {self._threshold}'
            )
            out = Bool()
            out.data = True
            self._pub.publish(out)


def main():
    rclpy.init()
    node = ThresholdAlarm()
    try:
        rclpy.spin(node)
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
