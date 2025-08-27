from sentence_transformers import SentenceTransformer

# 模型（英文论文适合使用这个多领域句向量模型）
model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')  # 或 'all-mpnet-base-v2'

def get_text_vectors(text):
    vectors = model.encode([text], device="cpu")[0].tolist()
    return vectors


if __name__ == '__main__':
    search_text = 'significantly influenced by both clouds and Earth’s surface temperature (EST)'
    get_text_vectors(search_text)
