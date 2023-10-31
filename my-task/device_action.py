import requests
url = "http://127.0.0.1:8000/tasks/dispatch_task"

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
								"waypoint": "charger2",
								"orientation": 0
							}
						}, {
							"category": "device_action",
							"description": {
								"device_id": "test_device_id",
                                "param_json_str":"test_param_json_str"
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
