from util.operation_excel import OperationExcel
from util.operation_json import OperationJson
from conf.yaml_config import YamlConfig


class GetData:

    def __init__(self, file_name=None):
        self.config = YamlConfig().YamlConfig
        self.opera_excel = OperationExcel(file_name=file_name)

    # 获取case_id
    def get_case_id(self, row):
        col = self.config['id']
        case_id = self.opera_excel.get_cell_value(row, col)
        if case_id == '':
            return None
        return case_id

    # 获取是否执行
    def get_is_run(self, row):
        flag = None
        col = self.config['case_exc']
        case_exc = self.opera_excel.get_cell_value(row, col)
        if case_exc == 'yes':
            flag = True
        else:
            flag = False
        return flag

    # 是否有header
    def get_is_header(self, row):
        col = self.config['header']
        header = self.opera_excel.get_cell_value(row, col)
        if header == 'yes':
            flag = True
        else:
            flag = False
        return flag

    # 获取请求方式
    def get_request_method(self, row):
        col = self.config['request_method']
        request_method = self.opera_excel.get_cell_value(row, col)
        return request_method

    # 获取url
    def get_url(self, row):
        col = self.config['url']
        url = self.opera_excel.get_cell_value(row, col)
        return url

    # 获取请求数据
    def get_request_data(self, row):
        col = self.config['request_data']
        request_data = self.opera_excel.get_cell_value(row, col)
        if request_data == '':
            return None
        return request_data

    # 获取被依赖case_id
    def get_case_be_depend(self, row):
        col = self.config['case_be_depend']
        case_be_depend = self.opera_excel.get_cell_value(row, col)
        if case_be_depend == '':
            return None
        return case_be_depend

    # 获取依赖id
    def get_case_depend(self, row):
        col = self.config['case_depend']
        case_depend = self.opera_excel.get_cell_value(row, col)
        if case_depend == '':
            return None
        return case_depend

    # 获取依赖数据
    def get_data_depend(self, row):
        col = self.config['data_depend']
        data_depend = self.opera_excel.get_cell_value(row, col)
        if data_depend == '':
            return None
        return data_depend

    # 获取依赖数据所属字段
    def get_field_depend(self, row):
        col = self.config['field_depend']
        field_depend = self.opera_excel.get_cell_value(row, col)
        if field_depend == '':
            return None
        return field_depend

    # 通过获取关键字拿到data数据
    def get_data_for_json(self, row):
        data_key = self.get_request_data(row)
        opera_json = OperationJson(file_name='test2')
        return opera_json.data[data_key]

    # 获取预期结果
    def get_expect_data(self, row):
        col = self.config['expect']
        expect = self.opera_excel.get_cell_value(row, col)
        if expect == '':
            return None
        return expect

    # 获取实际结果行号
    def get_result_col(self):
        return self.config['result']

    # 写入实际结果
    def write_result(self, row, result):
        col = self.config['result']
        self.opera_excel.save_to_excel_by_cell(row, col, result)

    # 获取表格行数
    def get_row_lines(self):
        return self.opera_excel.max_row
