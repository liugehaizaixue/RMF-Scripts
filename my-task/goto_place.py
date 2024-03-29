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
								"waypoint": "charger3",
								"orientation": 0
							}
						}, {
							"category": "wait_for",
							"description": {
								"duration": 1000
							}
						}]
				}
			}
            ,{
				"activity": {
					"category": "sequence",
					"description": {
						"activities": [{
							"category": "go_to_place",
							"description": {
								"waypoint": "charger4",
								"orientation": 0
							}
						}, {
							"category": "wait_for",
							"description": {
								"duration": 1000
							}
						}]
					}
				},
                "on_cancel":[{
						"category": "sequence",
						"description": {
							"activities": [{
								"category": "go_to_place",
								"description": {
									"waypoint": "charger1",
									"orientation": 0
								}
							}]
						}
				}]
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
