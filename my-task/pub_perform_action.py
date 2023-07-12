import requests
url = "http://127.0.0.1:8000/tasks/robot_task"

json = {
	"type": "robot_task_request",
    "robot": "tinyRobot1",
    "fleet": "tinyRobot",
	"request": {
		"category": "compose",
		"description": {
			"category": "teleop",
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
						}, {
							"category": "perform_action",
                            "description": {
                                "unix_millis_action_duration_estimate": 60000,
                                "category": "teleop",
                                "description": {},
                                "use_tool_sink": False
                            }
						}]
					}
				}
			}]
		},
		"unix_millis_earliest_start_time": 0,
		"priority": {
			"type": "binary",
			"value": 0
		}
	}
}
res = requests.post(url=url, json = json)
 
print("发送的body:",res.request.body)
print("response返回结果：",res.text)
