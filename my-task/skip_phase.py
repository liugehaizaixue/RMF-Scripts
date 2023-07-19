import requests
import json

url = "http://127.0.0.1:8000/tasks/skip_phase"
payload = {
  "type": "skip_phase_request",
  "task_id": "compose.dispatch-0",
  "phase_id": 1,
  "labels": [
    "string"
  ]
}

headers = {
    'Content-Type': 'application/json'
}

response = requests.post(url, data=json.dumps(payload), headers=headers)

print(response.text)

