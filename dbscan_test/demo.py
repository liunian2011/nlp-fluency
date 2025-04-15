import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.cluster import DBSCAN
from sklearn.decomposition import PCA

import file_resolver

def run_demo(file_contents):
    # 示例文本数据
    documents = [
        "Machine learning is amazing",
        "Deep learning is a subset of machine learning",
        "Artificial intelligence is the future",
        "AI and deep learning are revolutionizing industries",
        "I love playing football",
        "Soccer is known as football in Europe",
        "AI models are trained using data",
        "Machine learning is so amazing",
        "I like playing football ",

    ]

    # 1. 文本向量化（TF-IDF）
    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(file_contents)

    # 2. 计算余弦相似度并转换为距离矩阵
    cosine_sim = cosine_similarity(X)
    cosine_sim = (cosine_sim + 1) / 2  # 归一化到 [0,1]
    distance_matrix = np.clip(1 - cosine_sim, 0, None)  # 限制最小值为 0

    # 3. 运行 DBSCAN 聚类
    dbscan = DBSCAN(eps=0.4, min_samples=2, metric="precomputed")
    labels = dbscan.fit_predict(distance_matrix)

    # 4. 输出结果
    result = pd.DataFrame({"Text": file_contents, "Cluster": labels})
    print(result)

    '''
        # 4. 使用 PCA 进行降维
        import matplotlib.pyplot as plt
        import seaborn as sns
        
        pca = PCA(n_components=2)
        X_pca = pca.fit_transform(X.toarray())
    
        # 5. 画出聚类结果
        plt.figure(figsize=(8, 6))
        sns.scatterplot(x=X_pca[:, 0], y=X_pca[:, 1], hue=labels, palette="tab10", s=100, alpha=0.8)
        plt.title("DBSCAN Clustering of Texts (PCA Projection)")
        plt.xlabel("PCA Component 1")
        plt.ylabel("PCA Component 2")
        plt.legend(title="Cluster", loc="best")
        plt.show()
    '''

if __name__ == '__main__':
    json_file = '/mnt/geogpt/liunian/dbscan_demo/final_data.json'
    all_file_contents = file_resolver.read_all_files(json_file)
    print(all_file_contents)
    print('================')
    run_demo(all_file_contents)
