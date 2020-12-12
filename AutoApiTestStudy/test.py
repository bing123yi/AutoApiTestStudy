import requests
import json
import os

url = 'http://127.0.0.1:8000/login/'
data = {
    'username': 'testname',
    'password': '123214',

}
# print(os.path.abspath(os.path.dirname(__file__)))
# print(os.path.abspath(__file__))

# def send_post(url, data):
#     result = requests.post(url=url, data=data).json()
#     return json.dumps(result, indent=2, sort_keys=True)


file_dir = os.path.abspath(os.path.dirname(__file__))
file_path = file_dir + '\\test.txt'
file = open(file_path, 'r')
article = file.readlines()[0]
word_list = []
word = ''
word_dict = {}
word_count = {}
for i in article:
    if i not in [',', '.', ' ']:
        word += i
        # print(i)
        # print(word)
    else:
        if word != '':
            if word in word_count:
                word_count[word] += int(1)
            else:
                word_count[word] = 1
            word_list.append(word)
        word = ''
print(word_count)
for keys, values in dict.items():
    if values == values:
        print(keys, values)

for k, v in word_count:
    for key, value in word_count:
        if value > v:
            pass

# print(article)
