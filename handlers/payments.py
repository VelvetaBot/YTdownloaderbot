# payments.py

from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message

@Client.on_message(filters.command("premium"))
async def premium_info(client, message: Message):
    text = (
        "✨ *Premium Plan Details*\n\n"
        "🚀 Unlimited YouTube Downloads\n"
        "📱 A
