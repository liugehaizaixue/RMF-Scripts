import requests
import json

url = "http://127.0.0.1:8000/tasks/dispatch_task"

device_id = "transferRobot"
param_json = {
    "action":"lock"
}

json = {
	"type": "dispatch_task_request",
	"request": {
		"category": "compose",
		"description": {
			"category": "test_compose",
			"phases": [{
				"activity": {
					"category": "sequence",
					"description": [{
							"category": "go_to_place",
							"description": {
								"waypoint": "l1_2",
								"orientation": 0
							}
						}, {
							"category": "device_action",
							"description": {
								"device_id": device_id,
                                "param_json_str":json.dumps(param_json)
							}
						}]
				}
			}
            ]
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
