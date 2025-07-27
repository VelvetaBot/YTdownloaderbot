# profile.py

from pyrogram import Client, filters
from pyrogram.types import Message
from users import get_user_profile, is_premium
from language import get_user_language
from datetime import datetime

@Client.on_message(filters.command("profile") & filters.private)
async def user_profile(client, message: Message):
    user_id = message.from_user.id
    user_data = get_user_profile(user_id)
    lang = get_user_language(user_id)

    premium_status = "✅ Yes" if is_premium(user_id) else "❌ No"
    remaining_downloads = user_data.get("remaining", 0)
    reg_date = user_data.get("registered", "Unknown")
    if isinstance(reg_date, datetime):
        reg_date = reg_date.strftime("%d-%m-%Y")

    text = (
        f"👤 *Your Profile*\n\n"
        f"🆔 User ID: `{user_id}`\n"
        f"📅 Registered: {reg_date}\n"
        f"💎 Premium: {premium_status}\n"
        f"📥 Remaining Downloads: {remaining_downloads}/5\n"
        f"🌐 Language: {lang.upper()}"
    )

    await message.reply(text, parse_mode="markdown")
