import json
import datetime
import os
from urllib.parse import urlparse
from collections import Counter
import tldextract
from multiprocessing import Pool
import pagerank
from tqdm import tqdm
def extract_domain_old(url):
    """
    从URL中提取域名
    示例: https://www.example.com/path → example.com
    """
    parsed = urlparse(url)
    domain = parsed.netloc
    if domain.startswith('www.'):
        domain = domain[4:]
    return domain

def extract_domain(url):
    ext = tldextract.extract(url)
    # ext 是命名元组，包含: subdomain, domain, suffix
    # 例如 "blog.sub.example.co.uk" → subdomain="blog.sub", domain="example", suffix="co.uk"
    return f"{ext.domain}.{ext.suffix}"  # 组合主域名和顶级域

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

def cal_token_with_filter(file_path, domain_filter_path):
    token_summary_score_eval = {10:0, 9:0, 8:0, 7:0, 6:0}
    url_count = 0

    with open(domain_filter_path, 'r', encoding='utf-8') as f:
        all_domain_score = json.load(f)

    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            item = json.loads(line)
            dataset = item['data_set']
            metadata = item['meta_data']
            token = metadata['token_count']
            if dataset == 'dclm':
                url = metadata['warc_target_uri']
            elif dataset == 'fineweb':
                url = metadata['url']

            domain = extract_domain(url)

            if domain in all_domain_score:
                domain_score = all_domain_score[domain]
                if domain_score in [10,9,8,7,6]:
                    url_count += 1
                    token_summary_score_eval[domain_score] += domain_score

    print(f'url count:{url_count}')
    print(f'token_summary_score_eval: {token_summary_score_eval}')
    return token_summary_score_eval


def count_domain():
    file_path = '/mnt/geogpt/duyuxuan/file_web/dclm.jsonl'
    data1 = parse_jsonl_file(file_path)
    file_path2 = '/mnt/geogpt/duyuxuan/file_web/fineweb.jsonl'
    data2 = parse_jsonl_file(file_path)

    data = data1 + data2
    counter = Counter(data)
    top50 = counter.most_common()
    #counter.most_common()
    #print(top50)
    return top50


def test_domain():
    urls = [
        'www.sams.ac.uk',
        'wires.wiley.com',
        'www.senckenberg.de',
        'www.globalgeopark.org',
        'natural-resources.canada.ca',
        'english.igsnrr.cas.cn',
        'www.goyderinstitute.org',
        'earth.org',
        'www.ezilon.com',
        'www.aceee.org',
        'www.pacb.com',
        'm.csmonitor.com',
        'www.vcard.wur.nl',
        'www.nvwa.nl',
        'tackk.com',
    ]

    for url in urls:
        domain = extract_domain(url)
        print(f'url:{url}, \ndomain:{domain}')

def read_jsonl_in_batches(file_path, batch_size=1000):
    """生成器函数，分批读取JSONL文件"""
    batch = []
    count = 0
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            count += 1

            try:
                batch.append(json.loads(line.strip()))
                if len(batch) >= batch_size:
                    yield batch
                    batch = []
            except json.JSONDecodeError as e:
                print(f"Error decoding line: {e}")
                continue
        if batch:
            yield batch


def process_data(data):
    print(f'data:{data}')
    dataset = data['data_set']
    metadata = data['meta_data']
    if dataset == 'dclm':
        url = metadata['warc_target_uri']
    elif dataset == 'fineweb':
        url = metadata['url']
    else:
        url = None
    domain = extract_domain(url)
    metadata['domain'] = domain
    pr_values = pagerank.get_values([domain])
    print(f'pr value lenth:{len(pr_values)}')
    print(f'pr value:{pr_values}')
    metadata['page_rank_result'] = pr_values[0]

    return data

def process_batch(data):
    """
    处理批量JSON对象的示例函数
    可以根据实际需求修改
    """
    print(f'data length:{len(data)}')
    print(f'data:{data}')
    domain_list = []
    for item in data:
        dataset = item['data_set']
        metadata = item['meta_data']
        if dataset == 'dclm':
            url = metadata['warc_target_uri']
        elif dataset == 'fineweb':
            url = metadata['url']
        else:
            url = None
        domain = extract_domain(url)
        metadata['domain'] = domain
        domain_list.append(domain)

    print(f'domain:{domain_list}')
    pr_values = pagerank.get_values(domain_list)
    print(f'pr value lenth:{len(pr_values)}')
    if len(pr_values) == 1:
        print(f'get domain error.{pr_values}')
    print(f'pr value:{pr_values}')
    for index in range(0, len(data)):
        metadata = data[index]['meta_data']
        if len(data)==len(pr_values):
            pr_value = pr_values[index]
            metadata['page_rank_result'] = pr_value
        else:
            metadata['page_rank_result'] = {}

    return data

def parallel_process_jsonl(input_file, output_file, batch_size=100, workers=2):
    """并行处理JSONL文件"""
    with open(output_file, 'a', encoding='utf-8') as outfile:
        with Pool(workers) as pool:
            for batch in read_jsonl_in_batches(input_file, batch_size):
                #processed_batch = pool.map(process_data, batch)
                processed_batch = process_batch(batch)
                print(f'###processed batch size:{len(processed_batch)}')
                for item in processed_batch:
                    outfile.write(json.dumps(item, ensure_ascii=False) + '\n')


if __name__ == "__main__":
    file_path = '/mnt/geogpt/duyuxuan/file_web/dclm.jsonl'
    file_path2 = '/mnt/geogpt/duyuxuan/file_web/fineweb.jsonl'
    domain_score_path = '/mnt/geogpt/duyuxuan/file_web/final_pro_eval.json'
    #cal_token_with_filter(file_path, domain_score_path)
    file_path_rewrite = '/mnt/geogpt/duyuxuan/file_web/pagerank_output/fineweb_pr.jsonl'
    parallel_process_jsonl(file_path2, file_path_rewrite)

    #top = count_domain()
    #print(top)
