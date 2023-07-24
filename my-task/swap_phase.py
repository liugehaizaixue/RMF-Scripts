import json
import uuid
from rmf_task_msgs.msg import ApiRequest,ApiResponse
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
    _api_request_pub = node.create_publisher(ApiRequest,"/task_api_requests",transient_qos)


    _json_msg = {
            "type" : "swap_phase_request",
            "task_id":"compose.dispatch-0",
            "phase_a_id":111,
            "phase_b_id":111,
        }

    json.dump(_json_msg,stdout)
    request_uuid = "swapphase_"+str(uuid.uuid4())
    
    
    _api_request_pub.publish(ApiRequest(
            json_msg = json.dumps(_json_msg),
            request_id = request_uuid
        ))

if __name__ == '__main__':
    main()
