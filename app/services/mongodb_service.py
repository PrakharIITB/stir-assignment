from pymongo import MongoClient
from datetime import datetime
from app.config import Config

MONGODB_URI = Config.MONGODB_URI
DB_NAME = Config.DB_NAME
COLLECTION_NAME = Config.COLLECTION_NAME

client = MongoClient(MONGODB_URI)
db = client[DB_NAME]
collection = db[COLLECTION_NAME]

def save_to_mongodb(trends, ip_address):
    try:
        document = {
            "trends" : trends,
            "timestamp": datetime.now(),
            "ip_address": ip_address
        }
        result = collection.insert_one(document)
        return result.inserted_id
    finally:
        client.close()
