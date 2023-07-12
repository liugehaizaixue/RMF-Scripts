import sys
import uuid
import argparse
import json

import rclpy
from rclpy.node import Node
from rclpy.parameter import Parameter
from rclpy.qos import qos_profile_system_default

from rmf_fleet_msgs.msg import PathRequest, Location


###############################################################################

class Requester(Node):

    def __init__(self, argv=sys.argv):
        super().__init__('teleop_publisher')

        self.pub = self.create_publisher(
          PathRequest, 'robot_path_requests',
          qos_profile=qos_profile_system_default)

        msg = PathRequest()
        msg.fleet_name = 'tinyRobot'
        msg.robot_name = 'tinyRobot1'
        msg.task_id = str(uuid.uuid1())

        loc = Location()
        loc.x = float(9)
        loc.y = float(-25.0)
        loc.yaw = float(0)
        loc.level_name = "l1"
        msg.path.append(loc)
        self.pub.publish(msg)

###############################################################################


def main(argv=sys.argv):
    rclpy.init(args=sys.argv)
    args_without_ros = rclpy.utilities.remove_ros_args(sys.argv)

    requester = Requester(args_without_ros)
    rclpy.shutdown()


if __name__ == '__main__':
    main(sys.argv)
