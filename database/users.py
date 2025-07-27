# users.py

import json
import os
from datetime import datetime

USER_DB = "downloads/user_data.json"

# Ensure the folder exists
os.makedirs("downloads", exist_ok=True)

# Load user data
def load_users():
    if os.path.exists(USER_DB):
        with open(USER_DB, "r") as f:
            return json.load(f)
    return {}

# Save user data
def save_users(data):
    with open(USER_DB, "w") as f:
        json.dump(data, f, indent=4)

# Get user data by ID
def get_user_data(user_id):
    users = load_users()
    user_id = str(user_id)
    return users.get(user_id)

# Update user data
def update_user_data(user_id, downloads, date=None):
    users = load_users()
    user_id = str(user_id)
    if not date:
        date = datetime.today().strftime('%Y-%m-%d')
    users[user_id] = {
        "downloads": downloads,
        "last_download_date": date
    }
    save_users(users)

# Increment download count
def increment_user_download(user_id):
    data = get_user_data(user_id)
    today = datetime.today().strftime('%Y-%m-%d')
    if data is None or data["last_download_date"] != today:
        update_user_data(user_id, 1, today)
    else:
        update_user_data(user_id, data["downloads"] + 1, today)
