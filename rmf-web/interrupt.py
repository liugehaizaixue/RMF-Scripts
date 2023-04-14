import requests
import json

url = "http://127.0.0.1:8000/tasks/interrupt_task"
payload = {
  "type": "interrupt_task_request",
  "task_id": "compose.dispatch-2",
  "labels": [
    "string"
  ]
}

headers = {
    'Content-Type': 'application/json'
}

response = requests.post(url, data=json.dumps(payload), headers=headers)

print(response)

