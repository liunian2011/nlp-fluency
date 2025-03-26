import json
import os
import string
import clickhouse_connect
import numpy as np
import re


def is_non_english_char(char):
    # 判断是否为英文字符
    if char in string.ascii_letters:
        return False
    # 判断是否为特殊符号（包括空格、数字、标点符号等）
    if re.match(r'[\s\W_]', char):
        return False
    return True

def query_data(client, sql):
    query_result = client.query(sql)
    print(query_result.row_count)
    subject_list = []
    for result in query_result.result_set:
        subject = result[0]

        subject = subject.replace('\r\n', ' ').replace('\n', ' ')
        subject_list.append(subject)
        if is_non_english_char(subject):
            print(f'subject content:{subject}')
    return subject_list

def gen_dataset(label, geo_corpus_list):
    with open('./data/geo_train.txt', 'a') as f:
        for geo_corpus in geo_corpus_list:
            row = label + ', ' + geo_corpus + '\n'
            f.write(row)
            f.flush()


if __name__ == "__main__":
    client2 = clickhouse_connect.get_client(host="172.27.213.44", port=31238, username="zjlab", password="zjlab", database="scihub2")

    #sql = "SELECT concat_ws(',' ,ifNull(Subject,'') ,ifNull(Title,'') ,ifNull(SeriesTitle,'') ,ifNull(Keywords,'') , ifNull(Abstracts,'')) from scihub2.book_meta where Subject != ''"
    sql = "SELECT DISTINCT Abstract  FROM scihub2.scihub_meta AS t1 WHERE Subject = 'geography' and Abstract != '' and LENGTH(Abstract)> 60 limit 50000"
    #sql = "SELECT Abstract  FROM scihub2.scihub_meta AS t1 WHERE Subject = 'geography' and Abstract != '' and ID = 97385 limit 50000"
    subject_list = query_data(client2, sql)
    label1 = '__label__1'
    #gen_dataset(label1, subject_list)

    #sql2 = "select abstract from (select abstract from semantic.abstract limit 5000) a where a.abstract not like 'geograph'"
    sql2 = "SELECT DISTINCT Abstract  FROM scihub2.scihub_meta AS t1 WHERE t1.Subject = '' and Abstract != '' and LENGTH(Abstract)> 60 "
    #abstract_list = query_data(client2, sql2)
    #label2 = '__label__0'
    #gen_dataset(label2, abstract_list)
