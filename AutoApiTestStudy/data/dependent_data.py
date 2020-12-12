import json

def dependent_case_handle(res_data=None, data_depend=None):
    # opera_json = OperationJson(file_name='test2')
    # data_depend = 'data:items:8:item_id'
    # res_data = opera_json.read_data()

    handle_data = json.loads(res_data)
    keys = str.split(data_depend, ':')

    for i in range(len(keys)):
        if str.isdigit(keys[i]):
            key = int(keys[i])
        else:
            key = keys[i]
        handle_data = handle_data[key]
    return handle_data





