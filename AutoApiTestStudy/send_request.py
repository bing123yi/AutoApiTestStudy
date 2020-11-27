import requests
import json
from mock_package import mock_data

class SendRequest:

    def __init__(self):
        pass

    def send_request(self, url, method, data=None, header=None):
        if header is not None:
            if method == 'get':
                result = requests.get(url=url, headers=header, verify=False)
            elif method == 'post':
                result = requests.post(url=url, data=data, headers=header, verify=False)
        else:
            if method == 'get':
                result = requests.get(url=url, verify=False)
            elif method == 'post':
                result = requests.post(url=url, data=data, verify=False)
            else:
                result = 'wrong method'

        # 直接用mock写死返回数据
        # result = mock_data(url=url, request_data=None, method=method, response_data=data)

        # 获取接口返回状态码
        # print(result.status_code)

        return json.dumps(result.json(), indent=2, sort_keys=True)


if __name__ == '__main__':
    test = SendRequest()
    url = 'https://qilin.shentongcard.com/qilin/wxbear/ajaxIndex'

    print(test.send_request(url, 'get'))
