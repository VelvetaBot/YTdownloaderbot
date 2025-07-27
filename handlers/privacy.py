# privacy.py

from pyrogram import Client, filters
from pyrogram.types import Message

@Client.on_message(filters.command("privacy"))
async def privacy(client, message: Message):
    text = (
        "🔒 *Privacy Policy*\n\n"
        "We respect your privacy. This bot does not store your downloaded content or share your personal data with third parties.\n\n"
        "📌 Only essential data such as your user ID and download count is stored to enforce limits and manage premium access.\n\n"
        "For any concerns, contact the developer at @Yaswanth_venkata_naga_sai.\n\n"
        "_— Team Velvetta Bots_"
    )
    await message.reply(text, parse_mode="markdown", quote=True)
