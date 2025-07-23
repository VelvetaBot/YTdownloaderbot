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
            from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram import filters
from pyrogram.types import Message, CallbackQuery
import os
from database.users import increment_download, get_user_data, is_premium, save_download
import yt_dlp

# Button keyboard
def format_buttons(url):
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("📹 Video", callback_data=f"video|{url}")],
        [InlineKeyboardButton("🎵 Audio", callback_data=f"audio|{url}")]
    ])

def register(app):
    @app.on_message(filters.text & filters.private)
    async def ask_format(client, message: Message):
        url = message.text.strip()
        if "youtube.com" not in url and "youtu.be" not in url:
            return

        user = await get_user_data(message.from_user.id)
        if not await is_premium(message.from_user.id) and user["downloads_today"] >= 3:
            await message.reply("⚠️ You’ve reached your daily limit (3/day). Use /pay to upgrade.")
            return

        await message.reply("🔽 Select format to download:", reply_markup=format_buttons(url))

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
        from pyrogram import filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from database.users import get_user_data, is_premium, increment_download, save_download
import os, yt_dlp

def register(app):
    @app.on_message(filters.text & filters.private)
    async def ask_format(client, message: Message):
        url = message.text.strip()
        if "youtu" not in url:
            return

        # Store temporarily (optional: can use DB or RAM)
        client.cache = getattr(client, "cache", {})
        client.cache[message.from_user.id] = url

        # Send format selection
        await message.reply(
            "🎬 Choose format to download:",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("🎞 Video", callback_data="download_video")],
                [InlineKeyboardButton("🎵 Audio (MP3)", callback_data="download_audio")]
            ])
        )

    @app.on_callback_query(filters.regex("download_"))
    async def handle_format(client, query: CallbackQuery):
        user_id = query.from_user.id
        user = await get_user_data(user_id)

        if not await is_premium(user_id) and user["downloads_today"] >= 3:
            await query.message.edit("⚠️ Daily limit reached. Upgrade with /pay.")
            return

        url = getattr(client, "cache", {}).get(user_id)
        if not url:
            await query.message.edit("❌ URL expired. Please resend the YouTube link.")
            return

        format_type = query.data.split("_")[1]  # video or audio
        await query.message.edit(f"⏳ Downloading {format_type}...")

        try:
            file_path, title, size = await download_yt(url, format_type)
            if format_type == "video":
                await client.send_video(chat_id=user_id, video=file_path, caption=title)
            else:
                await client.send_audio(chat_id=user_id, audio=file_path, caption=title)

            await increment_download(user_id)
            await save_download(user_id, title, size)
            os.remove(file_path)

        except Exception as e:
            await query.message.edit(f"❌ Error: {e}")

# 🔧 Helper function
async def download_yt(url, format_type="video"):
    out_path = "downloads/%(title)s.%(ext)s"
    if format_type == "audio":
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': out_path,
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'quiet': True
        }
    else:  # video
        ydl_opts = {
            'format': 'best[ext=mp4]',
            'outtmpl': out_path,
            'quiet': True
        }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        filename = ydl.prepare_filename(info)
        size_mb = os.path.getsize(filename) / (1024 * 1024)
        return filename, info.get("title", "Your file"), size_mb
            @app.on_callback_query()
    async def handle_format(client, query: CallbackQuery):
        try:
            format_type, url = query.data.split("|", 1)
            await query.message.edit_text("⏳ Downloading, please wait...")

            file_path, title = await download_video(url, format_type)
            file_size = os.path.getsize(file_path) / (1024 * 1024)

            if format_type == "video":
                await query.message.reply_video(file_path, caption=title)
            else:
                await query.message.reply_audio(file_path, caption=title)

            os.remove(file_path)
            await increment_download(query.from_user.id)
            await save_download(query.from_user.id, title, file_size)

        except Exception as e:
            await query.message.reply(f"❌ Error: {e}")
async def download_video(url, format_type):
    ydl_opts = {
        'outtmpl': 'downloads/%(title)s.%(ext)s',
        'quiet': True
    }

    if format_type == "audio":
        ydl_opts.update({
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192'
            }]
        })
    else:  # video
        ydl_opts.update({'format': 'best[ext=mp4]'})

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        return ydl.prepare_filename(info), info.get('title', 'Your File')
        from database.users import is_banned

if await is_banned(message.from_user.id):
    await message.reply("🚫 You are banned from using this bot.")
    return






