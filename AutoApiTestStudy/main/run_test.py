from send_request import SendRequest
from data.get_data import GetData
from data.dependent_data import *
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
        be_depend_data = {}
        pass_count = []
        faile_count = []
        for i in range(2, rows_count):
            is_run = self.data.get_is_run(i)
            if is_run:
                # 获取Excel表第i行的数据
                url = self.data.get_url(i)
                request_method = self.data.get_request_method(i)
                request_data = self.data.get_request_data(request_method, i)
                header = self.data.get_header(i)
                expect_data = self.data.get_expect_data(i)
                case_be_depend = self.data.get_case_be_depend(i)
                case_depend = self.data.get_case_depend(i)

                if case_depend is not None:
                    # 数据依赖  直接从前面执行接口保存的数据中拿数据
                    # case_id = self.data.get_case_id(i)
                    if be_depend_data[case_depend] is not None:
                        data_depend = self.data.get_data_depend(i)
                        field_depend = self.data.get_field_depend(i)
                        depend_data = dependent_case_handle(be_depend_data[case_depend], data_depend)
                        # 将依赖的数据替换到请求数据字段中
                        request_data[field_depend] = depend_data

                    else:
                        raise ValueError('be_depend_data of the ' + str(case_depend) + 'is None')
                # 格式化 request_data
                request_data = self.data.format_request_data(request_method, request_data)

                # print(url)
                # print(request_method)
                # print(request_data)
                # print(header)
                # exit()
                # 执行接口请求
                res = self.send_request.send_request(url, request_method, request_data, header)
                # print(res)
                # exit()
                # 该case有被后续case数据依赖，先将接口返回数据存下来
                if case_be_depend is not None:
                    case_id = self.data.get_case_id(i)
                    be_depend_data[case_id] = res

                if expect_data is None:
                    result = '无预期结果，请检查'
                elif self.com_util.is_contain(expect_data, res):
                    result = '测试通过'
                    pass_count.append(i)
                else:
                    result = res
                    faile_count.append(i)
                self.data.write_result(i, result)
        print(pass_count)
        print(faile_count)
        return res


if __name__ == '__main__':
    test = RunTest()
    # test.dependent_case_handle()
    a = test.run_test()
