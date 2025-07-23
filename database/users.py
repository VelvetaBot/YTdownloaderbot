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
"plan": "free",
"premium_until": None,
from datetime import datetime, timedelta

# Check if user is premium
async def is_premium(user_id):
    user = users.find_one({"_id": user_id})
    if not user:
        return False
    if user["plan"] == "premium" and user["premium_until"]:
        expire_date = datetime.strptime(user["premium_until"], "%d.%m.%Y")
        if datetime.utcnow() <= expire_date:
            return True
        else:
            # Auto downgrade
            users.update_one({"_id": user_id}, {"$set": {"plan": "free", "premium_until": None}})
    return False

# Manually make someone premium for X days
async def make_premium(user_id, days=30):
    expire = (datetime.utcnow() + timedelta(days=days)).strftime("%d.%m.%Y")
    users.update_one(
        {"_id": user_id},
        {"$set": {"plan": "premium", "premium_until": expire}}
    (
        async def set_language(user_id, lang_code):
    users.update_one({"_id": user_id}, {"$set": {"language": lang_code}})

async def get_language(user_id):
    user = users.find_one({"_id": user_id})
    return user.get("language", "en") if user else "en"
    # Mark user as banned
async def ban_user(user_id):
    users.update_one({"_id": user_id}, {"$set": {"banned": True}})

async def unban_user(user_id):
    users.update_one({"_id": user_id}, {"$set": {"banned": False}})

async def is_banned(user_id):
    user = users.find_one({"_id": user_id})
    return user.get("banned", False)

# Get total user count
async def count_users():
    return users.count_documents({})




