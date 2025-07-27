# version.py

from pyrogram import Client, filters
from pyrogram.types import Message

BOT_VERSION = "1.0.0"
BUILD_DATE = "2025-07-22"
CREATOR = "Velvetta Bots"

@Client.on_message(filters.command("version") & filters.private)
async def version_info(client, message: Message):
    text = (
        f"🛠 **Velvetta Downloader Bot Info**\n\n"
        f"🔖 Version: `{BOT_VERSION}`\n"
        f"🛠 Build Date: `{BUILD_DATE}`\n"
        f"👨‍💻 Developer: `{CREATOR}`\n"
        f"📢 Channel: @Velvetabots"
    )

    await message.reply_text(text, quote=True)
