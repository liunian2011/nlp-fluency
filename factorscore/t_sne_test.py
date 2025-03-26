import numpy as np
import pandas as pd
from sklearn.manifold import TSNE
from sklearn.datasets import fetch_openml
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

# 加载 MNIST 数据集
mnist = fetch_openml('mnist_784', version=1)
X = mnist.data / 255.0  # 将数据归一化到 [0, 1] 区间
y = mnist.target

# 随机选择 10000 个数据点
np.random.seed(42)
indices = np.random.choice(X.shape[0], 10000, replace=False)
X_subset = X.iloc[indices]
y_subset = y.iloc[indices]

# 标准化数据
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X_subset)

# 应用 t-SNE 进行降维
tsne = TSNE(n_components=2, perplexity=30, n_iter=1000, random_state=42)
X_tsne = tsne.fit_transform(X_scaled)

# t-SNE 可视化结果
plt.figure(figsize=(12, 8))
scatter_tsne = plt.scatter(X_tsne[:, 0], X_tsne[:, 1], c=y_subset.astype(int), cmap='tab10', s=1)
plt.legend(*scatter_tsne.legend_elements(), title="Digits")
plt.title('MNIST 数据集的 t-SNE 可视化')
plt.xlabel('t-SNE 维度 1')
plt.ylabel('t-SNE 维度 2')
plt.show()
