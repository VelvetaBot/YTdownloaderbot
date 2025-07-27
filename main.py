import logging
from pyrogram import Client, filters

from config import API_ID, API_HASH, BOT_TOKEN

app = Client("yt_downloader_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

logging.basicConfig(level=logging.INFO)

@app.on_message(filters.command("start"))
async def start(client, message):
    await message.reply_text("👋 Hello! Send me a YouTube link and I will download it for you.")

@app.on_message(filters.text & ~filters.command("start"))
async def download(client, message):
    url = message.text
    await message.reply_text(f"⏳ Starting download for: {url}\n(This feature will be added soon!)")

app.run()
