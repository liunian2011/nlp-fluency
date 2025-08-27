import json



def read_jsonl_in_chunks(file_path, chunk_size=1000):
    """
    逐块读取大型JSONL文件的生成器函数

    参数:
        file_path: JSONL文件的路径
        chunk_size: 每个块包含的行数（记录数）

    返回:
        生成器，每次 yield 一个包含 chunk_size 条记录的列表
    """
    current_chunk = []
    with open(file_path, 'r', encoding='utf-8') as f:
        for line_num, line in enumerate(f, 1):
            # 跳过空行
            if not line.strip():
                continue
            try:
                data = json.loads(line)
                current_chunk.append(data)
            except json.JSONDecodeError as e:
                print(f"Warning: 在第 {line_num} 行解析JSON出错: {e}")
                # 可以选择跳过错误行或记录错误
                continue

            # 当块达到预定大小时，yield 并重置块
            if len(current_chunk) >= chunk_size:
                yield current_chunk
                current_chunk = [] # 重置当前块

        # 文件读取结束后，yield 最后不足 chunk_size 的剩余数据
        if current_chunk:
            yield current_chunk

# 使用示例
file_path = '/mnt/geogpt/liunian/geogpt-corpus/v0.9-20250616-43B.jsonl'
chunk_size = 1000 # 每次处理5000条记录


oa_paper_lines = []
oa_paper_limit = 300000
channel_set = set()
for chunk_id, chunk in enumerate(read_jsonl_in_chunks(file_path, chunk_size)):
    print(f"正在处理第 {chunk_id} 个块，包含 {len(chunk)} 条记录...")

    # 在这里对你的 chunk 数据进行处理
    # 例如：数据清洗、转换、批量入库等
    #process_chunk(chunk)

    for line_json in chunk:
        channel = line_json['channel']
        channel_set.add(channel)

        if channel == 'geo-oapaper':
            oa_paper_lines.append(line_json)

    if len(oa_paper_lines) > oa_paper_limit:
        break

print(f'all channel:{channel_set}')

oa_paper_jsonl_file_path = '/mnt/geogpt/liunian/geogpt-corpus/oa_paper_20250826.jsonl'

with open(oa_paper_jsonl_file_path, 'w', encoding='utf-8') as f:
    for oa_paper in oa_paper_lines:
        oa_paper_s = json.dumps(oa_paper)
        f.write(oa_paper_s)
        f.write('\n')