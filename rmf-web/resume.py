import requests
import json

url = "http://127.0.0.1:8000/tasks/resume_task"
payload = {
  "type": "resume_task_request",
  "for_task": "compose.dispatch-2",
  "for_tokens": [
    "0"
  ],
  "labels": [
    "string"
  ]
}

headers = {
    'Content-Type': 'application/json'
}

response = requests.post(url, data=json.dumps(payload), headers=headers)

print(response)

