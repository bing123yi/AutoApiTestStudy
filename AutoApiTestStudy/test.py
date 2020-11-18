import requests
import json

url = 'http://127.0.0.1:8000/login/'
data = {
    'username': 'testname',
    'password': '123214',

}


def send_post(url, data):
    result = requests.post(url=url, data=data).json()
    return json.dumps(result, indent=2, sort_keys=True)





