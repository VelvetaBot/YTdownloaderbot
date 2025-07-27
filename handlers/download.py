# download.py

from yt_dlp import YoutubeDL
from pyrogram import Client
from pyrogram.types import Message
from users import get_user_data, increment_user_download
from datetime import datetime

MAX_DAILY_DOWNLOADS = 5

def check_download_limit(user_id):
    user_data = get_user_data(user_id)
    today = datetime.today().strftime('%Y-%m-%d')

    if user_data is None or user_data["last_download_date"] != today:
        return True
    return user_data["downloads"] < MAX_DAILY_DOWNLOADS

def download_video(url: str):
    ydl_opts = {
        'format': 'best[ext=mp4]',
        'outtmpl': 'downloads/%(title)s.%(ext)s',
        'quiet': True,
    }

    with YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        filename = ydl.prepare_filename(info)
    return filename

async def handle_download(client: Client, message: Message, url: str):
    user_id = message.from_user.id

    if not check_download_limit(user_id):
        await message.reply_text(
            "😔 You've reached your *daily limit*.\n\n"
            "🚀 Unlock *unlimited downloads*, *fast speed*, and *Instagram support* with Premium!\n\n"
            "Send payment screenshot to our bot to get access.",
            disable_web_page_preview=True
        )
        return

    await message.reply_text("📥 Downloading your video, please wait...")

    try:
        file_path = download_video(url)
        await client.send_video(message.chat.id, video=file_path, caption="✅ Download complete!")
        increment_user_download(user_id)
    except Exception as e:
        await message.reply_text(f"❌ Download failed:\n{e}")
