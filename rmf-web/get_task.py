
import requests
 
url = "http://127.0.0.1:8000/tasks/compose.dispatch-0/state"

res = requests.get(url=url)
 
print("发送的body:",res.request.body)
print("response返回结果：",res.text)
