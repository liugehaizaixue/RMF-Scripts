import requests
import json

url = "http://127.0.0.1:8000/tasks/cancel_task"
payload = {
  "type": "cancel_task_request",
  "task_id": "compose.dispatch-0",
  "labels": [
    "string"
  ]
}

headers = {
    'Content-Type': 'application/json'
}

response = requests.post(url, data=json.dumps(payload), headers=headers)

print(response)

