import tldextract
import clickhouse_connect
from collections import Counter

def extract_domain(url):
    ext = tldextract.extract(url)
    # ext 是命名元组，包含: subdomain, domain, suffix
    # 例如 "blog.sub.example.co.uk" → subdomain="blog.sub", domain="example", suffix="co.uk"
    return f"{ext.domain}.{ext.suffix}"  # 组合主域名和顶级域

def query_data(client, sql):
    query_result = client.query(sql)

    url_list = []
    for result in query_result.result_set:
        url = result[0]
        url_list.append(url)
    print(f'url_list:{url_list}')

    return url_list


def gen_dataset(label, geo_corpus_list):
    with open('./data/geo_train.txt', 'a') as f:
        for geo_corpus in geo_corpus_list:
            row = label + ', ' + geo_corpus + '\n'
            f.write(row)
            f.flush()


def url_analysis_pipeline():
    client2 = clickhouse_connect.get_client(host="10.200.49.0", port=8123, username="zjlab", password="zjlab", database="scihub2")
    sql = "select DISTINCT url from scihub2.geo_search_data"
    url_list = query_data(client2, sql)

    domain_list = []
    for url in url_list:
        domain = extract_domain(url)
        domain_list.append(domain)

    counter = Counter(domain_list)
    top = counter.most_common()
    print(f'{top}')


if __name__ == "__main__":
    url_analysis_pipeline()


