import json
import requests

url = "http://10.200.99.220:32018/retrieve"

headers = {'Content-Type': 'application/json'}

data_str = """
{
    "text": "",
    "searchType":"embedding",
    "retrieveTopK":3
}
"""


def retrive(question, topk=3):
    data_json = json.loads(data_str)
    data_json['text'] = question
    data_json['retrieveTopK'] = topk
    response = requests.post(url, headers=headers, json=data_json)

    # 打印响应内容
    res_json = json.loads(response.text)
    code = res_json['code']
    data_list = res_json['data']
    text_all = ''
    for data in data_list:
        text_all += data['text']
        text_all += '\n\n'

    return text_all

if __name__ == '__main__':
    question = "Discuss the research content of reservoir heterogeneity and its influencing factors."
    text = retrive(question)
    print(text)