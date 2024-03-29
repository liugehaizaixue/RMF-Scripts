
import requests
url = "http://127.0.0.1:8000/tasks/robot_task"

json = {
	"type": "task_estimate_request",
    "fleet":"tinyRobot",
    "robot":"tinyRobot1",
	"request": {
		"category": "compose",
		"description": {
			"category": "test_compose",
			"phases": [{
				"activity": {
					"category": "sequence",
					"description": {
						"activities": [{
							"category": "go_to_place",
							"description": {
								"waypoint": "l1_6",
								"orientation": 0
							}
						}, {
							"category": "wait_for",
							"description": {
								"duration": 5000
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
