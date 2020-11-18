import requests
import json
from mock_package import mock_test

class sendRequest:

    def __init__(self):
        pass

    def send_request(self, url, method, data=None):
        if method == 'GET':
            result = requests.get(url=url).json()
        elif method == 'POST':
            result = requests.post(url=url, data=data).json()
        else:
            result = 'wrong method'
        return json.dumps(result, indent=2, sort_keys=True)


if __name__ == '__main__':
    test = sendRequest()
    url = 'http://127.0.0.1:8000/login/'
    data = {
        'username': 'test111name',
        'password': '12222222',

    }
    print(test.send_request(url, 'POST', data))
