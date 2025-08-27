from pymilvus import connections, utility
from pymilvus import FieldSchema, CollectionSchema, DataType, Collection

# 连接 Milvus 服务
connections.connect("default", host="10.200.49.1", port="9092")

# 获取服务版本
print("Milvus版本:", utility.get_server_version())

# 检查连接状态
print("现有集合列表:", utility.list_collections())

# 定义字段
fields = [
    FieldSchema(name="id", dtype=DataType.INT64, is_primary=True, auto_id=False),
    FieldSchema(name="vector", dtype=DataType.FLOAT_VECTOR, dim=128),
    FieldSchema(name="name", dtype=DataType.VARCHAR, max_length=50)
]

schema = CollectionSchema(fields, description="example collection")

# 创建 Collection
collection = Collection(name="demo_collection", schema=schema)