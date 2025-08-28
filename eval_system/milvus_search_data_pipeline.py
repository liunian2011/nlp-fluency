import csv
import os
import re
from tqdm import tqdm
import pandas as pd
import time
import milvus_db_manage


# 正则表达式
md_pattern = re.compile(r'Markdown Content:')
url_pattern = re.compile(
    r'(https?|ftp)://(www\.)?[-a-zA-Z0-9@:%._+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_+.~#?&/=]*)')


def parse_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        # 将换行替换为空格
        content = ' '.join([line.strip() for line in f.readlines()])

    # 取 Markdown Content:之后的内容
    match = md_pattern.search(content)
    start, end = match.span()
    content = content[end:]
    # 去除链接
    content = url_pattern.sub(' ', content)

    return content



def get_all_file(root_dir):
    print("开始遍历文件夹")
    file_paths = []
    start_time = time.time()
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if file.strip().endswith('.md'):
                file_paths.append(os.path.join(root, file))
    end_time = time.time()
    print(f'共用时{end_time - start_time}')
    return file_paths


def search_by_file(file_path):
    file_content = parse_file(file_path)
    if len(file_content) > 500:
        geo_pro_result = search_by_text(file_content)
        return geo_pro_result
    else:
        return None


def search_by_text(file_content):
    results = milvus_db_manage.search_data(file_content)
    distance = round(float(results[0][0].distance), 4)
    norm_distance = 1 - distance/2
    return norm_distance


def cal_geo_pro_scores(file_paths):
    prefix = '/mnt/geogpt/web_search/jina_url_data_processed'
    part_results = []
    for file_path in tqdm(file_paths):
        url_md5 = file_path.split('/')[-1][:-3]
        markdown = prefix + '/' + url_md5[:2] + '/' + url_md5[2:4] + '/' + url_md5 + '.md'

        geo_pro_result = search_by_file(file_path)
        if geo_pro_result:
            part_results.append((markdown, url_md5, geo_pro_result))

    part_df = pd.DataFrame(part_results, columns=["markdown", "url_md5", "geo_pro_result"])
    return part_df



if __name__ == '__main__':
    md_dir = "/mnt/geogpt/web_search/jina_url_data_processed/"
    md_files = get_all_file(md_dir)
    print(f'共搜索到{len(md_files)}个文件')

    #只取21000个进行测试
    if len(md_files) > 21000:
        valid_parts = md_files[0:21000]
        valid_length = len(valid_parts)
        print(f'当次要处理数量：{valid_length}')
    else:
        valid_pats = md_files

    valid_parts = valid_parts[0:10]

    start_time = time.time()
    geo_pro_df = cal_geo_pro_scores(valid_parts)
    end_time = time.time()
    print(f"共用时{end_time - start_time}秒")

    output_path = f"/mnt/geogpt/liunian/geo_pro_eval/geo_pro_web_search_result.csv"
    geo_pro_df.to_csv(output_path, encoding='utf-8', index=False, quoting=csv.QUOTE_NONNUMERIC)
    print(f"文件已保存在：{output_path},共{len(geo_pro_df)}条")