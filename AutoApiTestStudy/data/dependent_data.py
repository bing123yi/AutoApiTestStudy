from conf.yaml_config import YamlConfig
from util.operation_excel import OperationExcel


class DependentData:

    def __init__(self, file_name=None):
        self.config = YamlConfig().YamlConfig
        self.opera_excel = OperationExcel(file_name=file_name)

    # 通过case_id拿整行数据
    def get_depend_case_data(self, case_id):
        row = self.get_row_num(case_id)




    # 通过case_id的值拿到行号
    def get_row_num(self, case_id):
        case_id = str(case_id)
        col_dict = self.get_column_data('column_Id')
        # print(col_dict)
        # exit()
        return col_dict[case_id]


    def get_column_data(self, column_name):
        col_name = self.config[column_name]
        column_data = self.opera_excel.get_column_value(col_name)
        return column_data


if __name__ == '__main__':
    test = DependentData()
    print(test.get_row_num('login_3'))