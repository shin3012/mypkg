#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2025 Saito Shinnosuke
# SPDX-License-Identifier: BSD-3-Clause


import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16


class Talker(Node):
    def __init__(self):
        super().__init__('talker')
        self._publisher = self.create_publisher(Int16, 'countup', 10)
        self._timer = self.create_timer(0.5, self._on_timer)
        self._count = 0
        self.get_logger().info('talker started')

    def _on_timer(self):
        msg = Int16()
        msg.data = self._count
        self._publisher.publish(msg)
        self.get_logger().info(f'Publish: {msg.data}')
        self._count += 1


def main():
    rclpy.init()
    node = Talker()
    try:
        rclpy.spin(node)
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
