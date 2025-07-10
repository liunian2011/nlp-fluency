import redis
from rediscluster import RedisCluster
from tqdm import tqdm
from concurrent.futures import ThreadPoolExecutor

CHUNK_SIZE = 1000  # 每批处理1000条
DOMAIN_TO_INDEX_KEY_PREFIX = "cc:domain:"
INDEX_TO_DOMAIN_KEY_PREFIX = "cc:index:"

# Redis 连接
startup_nodes = [{"host": "10.200.49.1", "port": "6379"},
                 {"host": "10.200.49.2", "port": "6379"},
                 {"host": "10.200.49.3", "port": "6379"},
                 {"host": "10.200.49.4", "port": "6379"},
                 {"host": "10.200.49.5", "port": "6379"},
                 ]
rc = RedisCluster(startup_nodes=startup_nodes, password='d9eosTuv83', decode_responses=True)

def get_cluster():
    # Redis 连接
    startup_nodes = [{"host": "10.200.49.1", "port": "6379"},
                     {"host": "10.200.49.2", "port": "6379"},
                     {"host": "10.200.49.3", "port": "6379"},
                     {"host": "10.200.49.4", "port": "6379"},
                     {"host": "10.200.49.5", "port": "6379"},
                     ]
    rc = RedisCluster(startup_nodes=startup_nodes, password='d9eosTuv83', decode_responses=True)
    return rc

def write_key(key, value):
    rc.set(key, value)

def write_batch_data(csv_file_path):
    i = 0
    all_key_value = []
    # 读取CSV（无表头，空格或Tab分隔）
    with open(csv_file_path, encoding='utf-8') as f:
        for line in f:
            i += 1

            parts = line.strip().split()
            if len(parts) == 2:
                key_part = parts[1]
                key = INDEX_TO_DOMAIN_KEY_PREFIX + key_part
                value = parts[0]
                #rc.set(key, value)
                all_key_value.append((key, value))
            else:
                print(f'line {parts} format is wrong.')

    # 使用线程池并行写入
    with ThreadPoolExecutor(max_workers=8) as executor:
        for key,value in tqdm(all_key_value):
            executor.submit(write_key, key, value)
    print(f"Finished. Total rows processed:{i}")


def get_value(key:str):
    value = rc.get(key)
    return value

def get_index(domain:str):
    key = DOMAIN_TO_INDEX_KEY_PREFIX + domain
    return get_value(key)

def get_domain(index:str):
    key = INDEX_TO_DOMAIN_KEY_PREFIX + index
    return get_value(key)


if __name__ == "__main__":
    csv_path = '/mnt/geogpt/liunian/domain_analysis/metadata/pld-index'
    #write_batch_data(csv_path)
    print(get_index('baidu.com'))