# main.py

from pyrogram import Client
from config import API_ID, API_HASH, BOT_TOKEN, BOT_NAME

import logging

# Logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
LOGGER = logging.getLogger(__name__)

# Initialize Pyrogram Client
bot = Client(
    name=BOT_NAME,
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="plugins")
)

if __name__ == "__main__":
    LOGGER.info(f"Starting bot: {BOT_NAME}...")
    bot.run()
