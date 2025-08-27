from datasets import load_dataset
import pandas as pd
#
# # 加载数据集（在线下载）
# dataset = load_dataset("jsfactory/mental_health_reddit_posts", split="train")  # 例如 "imdb", "glue", "mnist"
#
# # 将 Dataset 转为 Pandas DataFrame
# df = dataset.to_pandas()
#
# # 保存为 CSV
# df.to_csv("./hf_local/imdb_train.csv", index=False)
# 保存到本地目录（默认保存为 Arrow/Parquet 格式）
#dataset.save_to_disk("./hf_local")  # 例如 "./data/imdb"



from huggingface_hub import hf_hub_download

# 下载 CSV 文件到本地
csv_path = hf_hub_download(
    repo_id="jsfactory/mental_health_reddit_posts",  # 数据集名称
    filename="posts.csv",  # 文件名
    repo_type="dataset",
    cache_dir="./hf_local/health_train.csv"  # 指定本地保存目录
)
print(f"CSV 文件已下载到：{csv_path}")