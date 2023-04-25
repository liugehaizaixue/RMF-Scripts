
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
								"waypoint": "room_1",
								"orientation": 0
							}
						}, {
							"category": "go_to_place",
							"description": {
								"waypoint": "corridor_4",
								"orientation": 0
							}
						},
							{
							"category": "go_to_place",
							"description": {
								"waypoint": "room_2",
								"orientation": 0
							}
						}
            ]
					}
				}
			},{
				"activity": {
					"category": "sequence",
					"description": {
						"activities": [{
							"category": "go_to_place",
							"description": {
								"waypoint": "corridor_4",
								"orientation": 0
							}
						}, {
							"category": "go_to_place",
							"description": {
								"waypoint": "room_1",
								"orientation": 0
							}
						}, {
							"category": "go_to_place",
							"description": {
								"waypoint": "start",
								"orientation": 0
							}
						}
            ]
					}
				}
			},
      ]
		},
		"unix_millis_earliest_start_time": 1681456523071, #任务开始时间 unix时间
		"priority": {  #优先级
			"type": "binary",
			"value": 0
		}
	}
}
res = requests.post(url=url, json = json)

