import json


class OperationJson:
    def __init__(self, file_path=None, file_name=None):
        if file_path is None:
            file_path = "D:/code/python/AutoApiTestStudy/dataconfig/"

        if file_name is None:
            file_name = "test3"
        self.json_file = file_path + file_name + '.json'
        self.data = None

    def read_data(self):
        # print(self.json_file)
        with open(self.json_file) as fp:
            self.data = json.load(fp)
            return self.data

    def get_json_data_by_key(self, key):
        return self.data[key]


if __name__ == '__main__':
    test = OperationJson()
    print(test.read_data())
