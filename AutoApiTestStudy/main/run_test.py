from send_request import SendRequest
from data.get_data import GetData
from util.common_util import CommonUtil
from util.operation_json import OperationJson


class RunTest:

    def __init__(self):
        self.data = GetData('api_test')
        self.send_request = SendRequest()
        self.com_util = CommonUtil()

    def run_test(self):
        rows_count = self.data.get_row_lines() + 1  # openpyxl行号是从1开始的
        res = None
        for i in range(2, rows_count):
            url = self.data.get_url(i)
            request_method = self.data.get_request_method(i)
            is_run = self.data.get_is_run(i)
            data = self.data.get_request_data(i)
            header = self.data.get_is_header(i)
            expect_data = self.data.get_expect_data(i)
            case_be_depend = self.data.get_case_be_depend(i)
            case_depend = self.data.get_case_id(i)
            res_data = {}
            if is_run:
                if case_depend is not None:
                    if res_data[case_depend] is not None:
                        data_depend = self.data.get_data_depend(i)
                        field_depend = self.data.get_field_depend(i)
                        data = self.dependent_case_handle(res_data[case_depend], data_depend, field_depend)
                    else:
                        pass

                res = self.send_request.send_request(url, request_method, data, header)
                # 该case有被后续case数据依赖，先将接口返回数据存下来
                if case_be_depend is not None:
                    case_id = self.data.get_case_id(i)
                    res_data[case_id] = res

                if self.com_util.is_contain(expect_data, res):
                    result = '测试通过'
                else:
                    result = '测试失败'
                self.data.write_result(i, result)
            # print(request_method)
            # print(data)
            # exit()
        return res

    def dependent_case_handle(self, res_data=None, data_depend=None, field_depend=None):
        opera_json = OperationJson(file_name='test2')
        data_depend = 'data:items:8:item_id'
        keys = str.split(data_depend, ':')
        res_data = opera_json.read_data()

        for i in range(len(keys)):
            if str.isdigit(keys[i]):
                key = int(keys[i])
            else:
                key = keys[i]
            res_data = res_data[key]
        print(res_data)

        data = None
        return data


if __name__ == '__main__':
    test = RunTest()
    test.dependent_case_handle()
    # print(test.run_test())
