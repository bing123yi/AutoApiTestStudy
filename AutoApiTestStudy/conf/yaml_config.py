import yaml
import os


class YamlConfig:

    def __init__(self):
        self.YamlConfig = self.excel_yaml()

    def excel_yaml(self):
        file_path = os.path.abspath(os.path.dirname(__file__))
        config_file = file_path + "\\config.yaml"
        with open(config_file, encoding='UTF-8') as fs:
            datas = yaml.load(fs)
            return datas


if __name__ == '__main__':
    test = YamlConfig()
    print(test.excel_yaml())
