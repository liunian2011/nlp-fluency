import json
import ast

def transfer_to_csv(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
        # 2. 用 ast.literal_eval 安全解析为 Python 对象（元组列表）
        data = ast.literal_eval(content)
        for item in data:
            domain = item[0]
            count = item[1]
            line = f"{domain},{count}\n"
            print(line)

def merge_csvs(path1, path2):
    with open(path1, 'r', encoding='utf-8') as f:
        content = f.read()
        # 2. 用 ast.literal_eval 安全解析为 Python 对象（元组列表）
        data1 = ast.literal_eval(content)

    with open(path2, 'r', encoding='utf-8') as f:
        content = f.read()
        # 2. 用 ast.literal_eval 安全解析为 Python 对象（元组列表）
        data2 = ast.literal_eval(content)

    merge_data = data1 + data2


if __name__ == "__main__":
    path = '/home/zjlab/code/nlp/fineweb_result.txt'
    transfer_to_csv(path)