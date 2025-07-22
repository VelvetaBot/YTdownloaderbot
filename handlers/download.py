from pyrogram import filters
from pyrogram.types import Message
import os
from database.users import increment_download, get_user_data
import yt_dlp

def register(app):
    @app.on_message(filters.text & filters.private)
    async def download(client, message: Message):
        url = message.text.strip()
        if "youtube.com" not in url and "youtu.be" not in url:
            return

        user = await get_user_data(message.from_user.id)
        if user["downloads_today"] >= 3:
            await message.reply("⚠️ You’ve reached your daily download limit.")
            return

        await message.reply("⏳ Downloading...")
        try:
            file_path = await download_video(url)
            await message.reply_video(file_path)
            os.remove(file_path)
            await increment_download(message.from_user.id)
        except Exception as e:
            from database.users import save_download

            await message.reply(f"❌ Error: {e}")

async def download_video(url):
    ydl_opts = {
        "outtmpl": "downloads/%(title)s.%(ext)s",
        "format": "best[ext=mp4]",
        "quiet": True
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        return ydl.prepare_filename(info)
        await message.reply_video(file_path)
file_size = os.path.getsize(file_path) / (1024 * 1024)
await message.reply_video(file_path)
await save_download(message.from_user.id, os.path.basename(file_path), file_size)
if user["downloads_today"] >= 3:
    await message.reply("⚠️ You’ve reached your daily download limit.")
    return
from database.users import is_premium

if not await is_premium(message.from_user.id):
    if user["downloads_today"] >= 3:
        await message.reply("⚠️ You’ve reached your daily limit (3/day). Upgrade to premium using /pay.")
        return



