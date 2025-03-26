from transformers import AutoModelForMaskedLM, AutoTokenizer

#model = AutoModelForMaskedLM.from_pretrained("bert-base-uncased")
#perplexity = exp(model(input_ids).loss.item())


from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np

# 示例数据：文本及情感标签（0=负面，1=正面）
texts = ["这部电影很棒", "糟糕的体验", "一般般", "推荐观看"]
labels = [1, 0, 0, 1]

# 文本向量化
tfidf = TfidfVectorizer()
X = tfidf.fit_transform(texts)
y = labels

print(f'x:{X}')
print(f'y:{y}')
# 划分训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25)

# 训练SVM（启用概率估计）
model = SVC(kernel='linear', probability=True)
model.fit(X_train, y_train)

# 预测测试集置信度
probas = model.predict_proba(X_test)  # 获取概率矩阵
predicted_class = model.predict(X_test)  # 预测类别
confidence_scores = probas.max(axis=1)  # 最大概率作为置信度

# 输出结果
for text, cls, conf in zip(texts, predicted_class, confidence_scores):
    print(f"文本: {text} | 预测类别: {cls} | 置信度: {conf:.2f}")