from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

# 加载本地模型（中文示例）
model = SentenceTransformer('BAAI/bge-small-en')  # BAAI/bge-m3 / m3e-base 等

geo_examples = []
non_geo_examples = []


with open('./datasource/train_data_case_10000.txt', 'r', encoding='utf-8') as f:
    for line in f:
        if line.startswith('__label__1'):
            pos_text = line.strip().replace('__label__1, ', '')
            geo_examples.append(pos_text)
        elif line.startswith('__label__0'):
            neg_text = line.strip().replace('__label__0, ', '')
            non_geo_examples.append(neg_text)

print(f'geo example len:{len(geo_examples)}')
print(f'non geo example len:{len(non_geo_examples)}')

# 编码示例
geo_vectors = model.encode(geo_examples, normalize_embeddings=True)
non_geo_vectors = model.encode(non_geo_examples, normalize_embeddings=True)
np.save('./emb_data/geo_vectors.npy', geo_vectors)  # 保存单个数组
np.save('./emb_data/non_geo_vectors.npy', non_geo_vectors)  # 保存单个数组

geo_vectors = np.load('./emb_data/geo_vectors.npy')
non_geo_vectors = np.load('./emb_data/non_geo_vectors.npy')

# 维度自动取自向量 shape
dimension = geo_vectors.shape[1]

# 创建向量库
geo_index = faiss.IndexFlatIP(dimension)
non_geo_index = faiss.IndexFlatIP(dimension)

geo_index.add(geo_vectors.astype(np.float32))
non_geo_index.add(non_geo_vectors.astype(np.float32))

to_judge_case_list = []

with open('./test_data_sample/eval_data_case_4000.txt', 'r', encoding='utf-8') as f:
    for line in f:
        if line.startswith('__label__1'):
            gr = 1
        elif line.startswith('__label__0'):
            gr = 0

        text = line.strip().replace('__label__0, ', '').replace('__label__1, ', '')
        eval_case = {'gr': gr, 'text': text}
        to_judge_case_list.append(eval_case)


i = 1
all_judge_list = []
for judge_case in to_judge_case_list:
    gr = judge_case['gr']
    text = judge_case['text']
    # 编码并归一化
    text_vector = model.encode([text], normalize_embeddings=True).astype(np.float32)

    print(f"text vector shaple:{text_vector.shape}")
    # 相似度搜索
    distance1, geo_sim = geo_index.search(text_vector, 1)
    distance2, non_geo_sim = non_geo_index.search(text_vector, 1)

    print(f"distance1:{distance1}, {geo_index.ntotal}, distance2:{distance2}, {non_geo_index.ntotal}")
    if geo_sim[0][0] > non_geo_sim[0][0]:
        print(f"{i}: 判断结果：地学. Geo similarity: {geo_sim[0][0]:.4f}, Non-geo similarity: {non_geo_sim[0][0]:.4f}")
        judge_output = 1
    else:
        print(f"{i}: 判断结果：非地学. Geo similarity: {geo_sim[0][0]:.4f}, Non-geo similarity: {non_geo_sim[0][0]:.4f}")
        judge_output = 0

    is_judge_right = 1 if gr == judge_output else 0
    all_judge_list.append(is_judge_right)
    i += 1

print(f'总数：{len(all_judge_list)}, 正确数：{all_judge_list.count(1)}, 错误数：{all_judge_list.count(0)}')