import configparser
import os

class IniConfig:

    def __init__(self):

        self.cf = configparser.ConfigParser()


    def read_ini(self):
        file_path = os.path.abspath(os.path.dirname(__file__))
        config_file = file_path + "\\config.ini"
        self.cf.read(config_file)
        data = self.cf.get('server', 'test')
        return data




if __name__ == '__main__':
    test = IniConfig()
    a = test.read_ini()
    print(a)