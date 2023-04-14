
import requests
 
url = "http://127.0.0.1:8000/tasks/dispatch_task"
json ={
    "type": "dispatch_task_request",
    "request": {
        "unix_millis_earliest_start_time": 1673510416754,
        "category": "pickup",
        "description": {
        "pickup": {
            "place": "start",
            "handler": "coke_dispenser",
            "payload": []
            }
        }
    }
}
res = requests.post(url=url, json = json)
 
print("发送的body:",res.request.body)
print("response返回结果：",res.text)
