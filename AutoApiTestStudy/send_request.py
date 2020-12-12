import requests
import json
from mock_package import mock_data


class SendRequest:

    def __init__(self):
        pass

    def send_request(self, url, method, request_data=None, header=None):
        if header is not None:
            if method == 'get':
                result = requests.get(url=url + request_data, headers=header, verify=False)
            elif method == 'post':
                result = requests.post(url=url, data=request_data, headers=header, verify=False)
        else:
            if method == 'get':
                result = requests.get(url=url + request_data, verify=False)
            elif method == 'post':
                result = requests.post(url=url, data=request_data, verify=False)
            else:
                result = 'wrong method'

        # 直接用mock写死返回数据
        # result = mock_data(url=url, request_data=None, method=method, response_data=data)

        # 获取接口返回状态码
        # print(result.status_code)

        return json.dumps(result.json(), indent=2, sort_keys=True)


if __name__ == '__main__':
    test = SendRequest()
    # url = 'https://care.seewo.com/easicare/account/v2/login'
    # request_data = json.dumps({'userName': '10156121201', 'password': 'e10adc3949ba59abbe56e057f20f883e'})
    # print(request_data)
    # header = {'appKey': 'easicare-ios', 'Content-Type': 'application/json',
    #           'deviceId': '917DB1EB-B6E5-4325-BD5D-8A87AC9FACD7'}
    # print(test.send_request(url, 'post', request_data, header))
