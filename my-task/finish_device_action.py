import json
import uuid
from rmf_device_msgs.msg import DeviceResult
import rclpy
from rclpy.node import Node

from rclpy.qos import QoSProfile
from rclpy.qos import QoSHistoryPolicy as History
from rclpy.qos import QoSDurabilityPolicy as Durability
from rclpy.qos import QoSReliabilityPolicy as Reliability
from sys import stdout


def main(args=None):
    rclpy.init(args=args)
    transient_qos = QoSProfile(
        history=History.KEEP_LAST,
        depth=1,
        reliability=Reliability.RELIABLE,
        durability=Durability.TRANSIENT_LOCAL)
    node = rclpy.create_node('robot_state_publisher')
    _api_request_pub = node.create_publisher(DeviceResult,"/device_results",transient_qos)


    
    request_guid = "compose.dispatch-0"
    status = 1
    
    _api_request_pub.publish(DeviceResult(
            time=node.get_clock().now().to_msg(),
            request_guid = request_guid,
            status = status
        ))

if __name__ == '__main__':
    main()
