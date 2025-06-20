from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["db_widecolumn"]
collection = db["students"]

# Hapus data lama (opsional)
collection.delete_many({})

# Masukkan 5 data baru
students = [
    {"id": 101, "nama": "Fajar", "matematika": 78, "b_indonesia": 82, "ipa": 85},
    {"id": 102, "nama": "Gita", "matematika": 88, "b_indonesia": 90, "ipa": 91},
    {"id": 103, "nama": "Hana", "matematika": 92, "b_indonesia": 85, "ipa": 87},
    {"id": 104, "nama": "Iwan", "matematika": 70, "b_indonesia": 75, "ipa": 80},
    {"id": 105, "nama": "Joko", "matematika": 65, "b_indonesia": 68, "ipa": 72}
]

collection.insert_many(students)

# Tampilkan data
for doc in collection.find():
    print(doc)
