from datasketch import MinHash, MinHashLSH
from sklearn.feature_extraction.text import CountVectorizer

# 示例：两段文本的重复性检测
text1 = "该地层为中生代砂岩，夹泥岩夹层"
text2 = "中生代砂岩夹泥岩出现在本地层序中"
text3 = "中生代砂岩夹泥岩出现在本地层序"

texts = [text1, text2, text3]  # 你的 text 列表（字符串）

def get_minhash(text, num_perm=128, shingle_size=4):
    shingles = set([text[i:i+shingle_size] for i in range(len(text) - shingle_size + 1)])
    m = MinHash(num_perm=num_perm)
    for s in shingles:
        m.update(s.encode('utf8'))
    return m

lsh = MinHashLSH(threshold=0.8, num_perm=128)
minhashes = {}

for i, text in enumerate(texts):
    m = get_minhash(text)
    lsh.insert(f"text_{i}", m)
    minhashes[f"text_{i}"] = (text, m)

duplicate_groups = []
visited = set()

for key, (text, m) in minhashes.items():
    if key in visited:
        continue
    duplicates = lsh.query(m)
    group = [minhashes[k][0] for k in duplicates]
    if len(group) > 1:
        duplicate_groups.append(group)
        visited.update(duplicates)

for group in duplicate_groups:
    print("重复组：")
    for text in group:
        print(" -", text)





