#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from sys import api_version, stdout
from rmf_device_msgs.msg import *
import rclpy
from rclpy.node import Node

from rclpy.qos import QoSProfile
from rclpy.qos import QoSHistoryPolicy as History
from rclpy.qos import QoSDurabilityPolicy as Durability
from rclpy.qos import QoSReliabilityPolicy as Reliability

from sched import scheduler
import time 
import threading
import json
import uuid
import eventlet

class PseudoDevice(Node):
    """
    - 周期性公布 `DeviceState`
    - 听 `DeviceRequest`
    - 发 `DeviceResult`

    接受 rmf server-> Device_req 之后,
    执行相应操作
    然后再返回device_state Device_result"""

    def __init__(self, name : str = "pseudo_device"):
        super().__init__(name)
        self._name = name
        self._processed_guid = {}
        self._device_state_pub = self.create_publisher(DeviceState,"/device_states",10)

        transient_qos = QoSProfile(
            history=History.KEEP_LAST,
            depth=1,
            reliability=Reliability.RELIABLE,
            durability=Durability.TRANSIENT_LOCAL)


        self._device_request_sub = self.create_subscription(DeviceRequest,"/device_requests",lambda msg: self.device_request_cb(msg),10)
        self._device_result_pub = self.create_publisher(DeviceResult,"/device_results",10)

        
        self.res_msg = DeviceResult()
        self._guid = "<undefined>"
        self._current_state = DeviceState(guid = self._name,mode = DeviceState.IDLE)
        self._past_request_guids = []
        self._mutex = threading.Lock()




    def device_request_cb(self,msg : DeviceRequest):
        if msg.target_guid != self._name:
            print("request neglected because" ,msg.target_guid ," != ",self._name)
            return 
        print("received request")
        if self._processed_guid.get(msg.request_guid) is not None:
            print("already given to ",msg.request_guid)
            return
        print(msg)
        self._processed_guid[msg.request_guid] = 0

        param_json = json.loads(msg.param_json_str)
        action = param_json["action"]
        param = param_json["param"]
        print("action",action)
        print("param",param)
        self.do_action()

        with self._mutex:
            self._processed_guid[msg.request_guid] = 21
            try :
                with eventlet.Timeout(120):
                    res_msg = DeviceResult(
                        request_guid = msg.request_guid,
                        source_guid = self._name,
                        status = DeviceResult.SUCCESS,
                        time=self.get_clock().now().to_msg()
                    )

            except eventlet.TimeoutError:
                self.res_msg = DeviceResult(
                    request_guid = msg.request_guid,
                    source_guid = self._name,
                    status = DeviceResult.FAILED,
                    time = self.get_clock().now().to_msg()
                )

            for i in range(3): # 加个循环
                self._device_result_pub.publish(res_msg)
                time.sleep(1)


    def do_action(self):
        print("执行相应操作")
        pass

    def publish_state(self):
        with self._mutex:
            self._device_state_pub.publish(DeviceState(
                time = self.get_clock().now().to_msg(),
                guid = self._name,
                mode = DeviceState.IDLE,
                request_guid_queue = [],
                seconds_remaining = 0.0
            ))
    
    def update(self):
        with self._mutex:
            to_del = [] 
            print(self._processed_guid)
            for (k,t) in self._processed_guid.items():
                if t > 20:
                    to_del.append( k)
                    continue
                self._processed_guid[k] +=1
                
            for k in to_del:
                del self._processed_guid[k]
                pass
            pass

def cycling(psd: PseudoDevice):
    while(True):
        psd.publish_state()
        psd.update()
        time.sleep(1)
        pass



if __name__ == "__main__":

    rclpy.init()
    #创建节点
    node = PseudoDevice("mechanical_arm_1")

    # Create executor for the command handle node
    rclpy_executor = rclpy.executors.MultiThreadedExecutor(3)
    rclpy_executor.add_node(node)
    th = threading.Thread(target=cycling, args=(node,) )
    th.start()
    # Start the fleet adapter
    rclpy_executor.spin()

    # Shutdown
    node.destroy_node()
    rclpy_executor.shutdown()
    rclpy.shutdown()
