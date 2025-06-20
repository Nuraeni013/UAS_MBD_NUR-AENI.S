from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["db_keyvalue"]
collection = db["kv_store"]

# Hapus data lama (opsional)
collection.delete_many({})

# Masukkan 5 data baru
data = [
    {"key": "product:101", "value": "Laptop"},
    {"key": "product:102", "value": "Smartphone"},
    {"key": "product:103", "value": "Tablet"},
    {"key": "product:104", "value": "Headphones"},
    {"key": "product:105", "value": "Smartwatch"}
]

collection.insert_many(data)

# Tampilkan data
for doc in collection.find():
    print(doc)
