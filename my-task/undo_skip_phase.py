import requests
import json

url = "http://127.0.0.1:8000/tasks/undo_skip_phase"
payload = {
  "type": "undo_phase_skip_request",
  "for_task": "compose.dispatch-0",
  "for_tokens": [
    "0","1"
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

