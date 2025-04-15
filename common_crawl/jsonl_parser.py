import json
import os
from urllib.parse import urlparse
from collections import Counter

def extract_domain(url):
    """
    从URL中提取域名
    示例: https://www.example.com/path → example.com
    """
    parsed = urlparse(url)
    domain = parsed.netloc
    #if domain.startswith('www.'):
    #    domain = domain[4:]
    return domain

def parse_jsonl_file(file_path):
    """解析单个 JSONL 文件"""
    data = []

    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            item = json.loads(line)
            dataset = item['data_set']
            metadata = item['meta_data']
            if dataset == 'dclm':
                url = metadata['warc_target_uri']
            elif dataset == 'fineweb':
                url = metadata['url']
            else:
                url = None
            domain = extract_domain(url)
            data.append(domain)

        '''
        for line in f:
            try:
                line_list = eval(line)
                for item in line_list:
                    dataset = item['data_set']
                    metadata = item['meta_data']
                    if dataset == 'dclm':
                        url = metadata['warc_target_uri']
                    elif dataset == 'fineweb':
                        url = metadata['url']
                    else:
                        url = None

                    domain = extract_domain(url)
                    #data.append({'url':url, 'domain':domain})
                    data.append(domain)
            except json.JSONDecodeError as e:
                print(f"Error parsing line in {file_path}: {e}")
                continue
        '''
    return data

def summary_token(file_path):
    token_summary = 0

    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            item = json.loads(line)
            metadata = item['meta_data']
            token = metadata['token_count']
            token_summary += token
    print(f'{file_path} token summary:{token_summary}')

def process_directory(directory):
    """递归处理目录中的所有 JSONL 文件"""
    all_data = []

    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.jsonl'):
                file_path = os.path.join(root, file)
                print(f"Processing: {file_path}")
                file_data = parse_jsonl_file(file_path)
                all_data.extend(file_data)

    return all_data

if __name__ == "__main__":
    file_path = '/mnt/geogpt/duyuxuan/file_web/dclm.jsonl'
    #data1 = parse_jsonl_file(file_path)
    file_path2 = '/mnt/geogpt/duyuxuan/file_web/fineweb.jsonl'
    #data2 = parse_jsonl_file(file_path)

    #data = data1 + data2
    #counter = Counter(data)
    #top50 = counter.most_common(500)
    #print(top50)
    summary_token(file_path)
    summary_token(file_path2)