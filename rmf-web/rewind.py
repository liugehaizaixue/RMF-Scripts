import requests
import json

url = "http://127.0.0.1:8000/tasks/rewind_task"
payload = {
    "type": "rewind_task_request",
    "task_id": "compose.dispatch-0",
    "phase_id": 0
}

headers = {
    'Content-Type': 'application/json'
}

response = requests.post(url, data=json.dumps(payload), headers=headers)

print(response)

