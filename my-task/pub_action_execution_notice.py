import rclpy
from rmf_fleet_msgs.msg import RobotMode,ModeRequest

""" 
发送ModeRequest 到 /action_execution_notice 会结束当前perform
        if msg.mode.mode == RobotState.IDLE:
            self.complete_robot_action()
"""
def send_msg():
    # 创建ROS节点
    rclpy.init()
    node = rclpy.create_node('pub_action_execution_notice')

    # 创建消息发布者
    msg_publisher = node.create_publisher(ModeRequest, '/action_execution_notice', 10)

    # 创建消息对象
    _msg = ModeRequest()

    # 填充消息字段
    _msg.fleet_name = "tinyRobot"
    _msg.robot_name = "tinyRobot1"
    _msg.mode.mode = RobotMode.MODE_IDLE 

    _msg.task_id = "custom_action_a34b0286-8d7d-4b9d-a3ca-c6b41b47d93e"


    # 发布消息
    msg_publisher.publish(_msg)

    # 关闭节点
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    send_msg()
