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

    node = rclpy.create_node('robot_state_publisher')
    _api_request_pub = node.create_publisher(ApiRequest,"/task_api_requests",transient_qos)
    transient_qos = QoSProfile(
        history=History.KEEP_LAST,
        depth=1,
        reliability=Reliability.RELIABLE,
        durability=Durability.TRANSIENT_LOCAL)

    fleet = "tinyRobot"
    robot = "tinyRobot1"

    place = "room_2"
    handler = "coke_handler"

    _json_msg = {
            "type" : "robot_task_request",
            "robot":robot,
            "fleet":fleet,
            "request" : {
                "unix_millis_earliest_start_time" : 0,
                "category" : "pickup",
                "task_priority":{
                    "type": "binary",
                    "value": 4
                },
                "description":{
                    "pickup":{
                        "place":place,
                        "handler":handler,
                        "payload":[] # "coke,1", "coke,2"
                    }
                }
            }
        }

    json.dump(_json_msg,stdout)
    request_uuid = "pickup_"+str(uuid.uuid4())
    
    _api_request_pub.publish(ApiRequest(
            json_msg = json.dumps(_json_msg),
            request_id = request_uuid
        ))

