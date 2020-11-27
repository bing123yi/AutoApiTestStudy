import mock


def mock_data(response_data, request_data=None, url=None, method=None):
    response_data = {
        'response_data': '7823212',
        'method': 'I love U!'
    }
    mock_method = mock.Mock(return_value=response_data)
    res = mock_method(url, method, request_data)
    return res
