import re
import time
from tqdm import tqdm
import clickhouse_connect

blank_pattern = re.compile(r'\s+')


def clean_text(text):
    new_text = blank_pattern.sub(' ', text)
    return new_text.strip()

def query_data(client, sql):
    query_result = client.query(sql)

    url_list = []
    for result in query_result.result_set:
        url = result[0]
        url_list.append(url)
    return url_list

client = clickhouse_connect.get_client(host = "10.200.49.0", port = 8123, username = "geogpt_data", password = "G8@data#501lmlj", database = "scihub2")

# - pos
scihub_pos_sql = f"""SELECT Abstract from scihub2.scihub_meta sm where Subject = 'geography' and Abstract != '' limit 200000 """
scihub_pos_results = query_data(client, scihub_pos_sql)
print('查询scihub正样本数据，共: ', len(scihub_pos_results))

# - neg
book_neg_sql = f"""SELECT Abstract from scihub2.scihub_meta sm where Subject != 'geography' and Abstract != '' """
book_neg_results = query_data(client, book_neg_sql)
print('查询scihub负样本数据，共: ', len(book_neg_results))

with open('train_data/scihub_pos_train_data.txt', 'w', encoding='utf-8') as f:
    for abstract in tqdm(scihub_pos_results):
        clean_abstract = clean_text(abstract)
        f.write('__label__1, ' + clean_abstract + '\n')
print(f'scihub正样本已保存在: train_data/scihub_pos_train_data.txt')

with open('train_data/scihub_neg_train_data.txt', 'w', encoding='utf-8') as f:
    for abstract in tqdm(book_neg_results):
        clean_abstract = clean_text(abstract)
        f.write('__label__0, ' + clean_abstract + '\n')
print(f'scihub负样本已保存在: train_data/scihub_neg_train_data.txt')

