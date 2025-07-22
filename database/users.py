from datetime import datetime
from pymongo import MongoClient
from config import MONGO_URL

client = MongoClient(MONGO_URL)
db = client.ytdl_bot
users = db.users

async def add_user(user):
    if not users.find_one({"_id": user.id}):
        users.insert_one({
            "_id": user.id,
            "username": user.username,
            "first_name": user.first_name,
            "last_name": user.last_name or "",
            "join_date": datetime.utcnow().strftime("%d.%m.%Y %H:%M:%S"),
            "downloads_today": 0,
        })

async def get_user_data(user_id):
    return users.find_one({"_id": user_id})

async def increment_download(user_id):
    users.update_one({"_id": user_id}, {"$inc": {"downloads_today": 1}})
    from datetime import datetime

# Save history of each downloaded video
async def save_download(user_id, title, size_mb):
    users.update_one(
        {"_id": user_id},
        {
            "$push": {
                "history": {
                    "title": title,
                    "size": f"{size_mb:.2f} MB",
                    "time": datetime.utcnow().strftime("%d.%m.%Y %H:%M")
                }
            }
        }
    )
"downloads_today": 0,
"history": []


