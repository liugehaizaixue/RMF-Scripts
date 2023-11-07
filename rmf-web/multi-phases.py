
import requests
url = "http://127.0.0.1:8000/tasks/dispatch_task"

json = {
	"type": "dispatch_task_request",
	"request": {
		"category": "compose",
		"description": {
			"category": "example_for_gotoplace",
			"phases": [{
				"activity": {
					"category": "sequence",
					"description": {
						"activities": [{
							"category": "go_to_place",
							"description": {
								"waypoint": "l1_1",
								"orientation": 0
							}
						},{
							"category": "wait_for",
							"description": {
								"duration": 500000
						}
                        }]
					}
				}
			},{
				"activity": {
					"category": "sequence",
					"description": {
						"activities": [ {
							"category": "go_to_place",
							"description": {
								"waypoint": "l1_7",
								"orientation": 0
							}
						},{
							"category": "wait_for",
							"description": {
								"duration": 500000
						}
                        }]
					}
				}
			},{
				"activity": {
					"category": "sequence",
					"description": {
						"activities": [{
							"category": "wait_for",
							"description": {
								"duration": 100 #如果skip的是当前phase并且是最后一个phase时，将显示任务状态为canceled,因此建议每个任务末尾添加一个 没有实际意义的waitfor（0.1s）phase，使其正常结束
						}
                        }]
					}
				}
			}
      ]
		},
		"unix_millis_earliest_start_time": 0, #任务开始时间 unix时间
		"priority": {  #优先级
			"type": "binary",
			"value": 0
		}
	}
}
res = requests.post(url=url, json = json)

print("返回的任务id为： "+res.json()["state"]["booking"]["id"])