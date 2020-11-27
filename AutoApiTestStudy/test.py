import requests
import json
import os

url = 'http://127.0.0.1:8000/login/'
data = {
    'username': 'testname',
    'password': '123214',

}
print(os.path.abspath(os.path.dirname(__file__)))
print(os.path.abspath(__file__))

def send_post(url, data):
    result = requests.post(url=url, data=data).json()
    return json.dumps(result, indent=2, sort_keys=True)





