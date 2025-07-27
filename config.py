# config.py

import os

API_ID = int(os.environ.get("API_ID", 11253846))
API_HASH = os.environ.get("API_HASH", "8db4eb50f557faa9a5756e64fb74a51a")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7523588106:AAHLLbwPCLJwZdKUVL6gA6KNAR_86eHJCWU")

# Channel and Support
CHANNEL_LINK = os.environ.get("CHANNEL_LINK", "https://t.me/Velvetabots")
SUPPORT_LINK = os.environ.get("SUPPORT_LINK", "https://t.me/Yaswanth_venkata_naga_sai")

# Admin
ADMIN_ID = int(os.environ.get("ADMIN_ID", 883128927))

# Daily Limit
DAILY_DOWNLOAD_LIMIT = int(os.environ.get("DAILY_DOWNLOAD_LIMIT", 5))

# Premium
PREMIUM_PRICE = int(os.environ.get("PREMIUM_PRICE", 49))  # ₹49
PREMIUM_DAYS = int(os.environ.get("PREMIUM_DAYS", 60))    # 60 days

# MongoDB URI (Render Environment variable)
MONGO_URI = os.environ.get("MONGO_URI", "mongodb://localhost:27017")
DATABASE_NAME = os.environ.get("DATABASE_NAME", "velveta_db")

# General
BOT_NAME = os.environ.get("BOT_NAME", "Velveta Bots")
