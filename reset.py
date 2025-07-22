from pymongo import MongoClient
from config import MONGO_URL

client = MongoClient(MONGO_URL)
db = client.ytdl_bot
users = db.users

def reset_downloads():
    users.update_many({}, {"$set": {"downloads_today": 0}})
    print("✅ Daily download counters reset.")
