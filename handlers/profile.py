# profile.py

from pyrogram import Client, filters
from pyrogram.types import Message
from users import get_user_data

@Client.on_message(filters.command("profile"))
async def profile(client, message: Message):
    user_id = message.from_user.id
    data = get_user_data(user_id)

    is_premium = "✅ Yes" if data["is_premium"] else "❌ No"
    downloads = data["downloads"]
    max_limit = "∞ Unlimited" if data["is_premium"] else "5 per day"

    text = (
        f"👤 *Your Profile*\n\n"
        f"🆔 ID: `{user_id}`\n"
        f"💎 Premium: {is_premium}\n"
        f"📥 Downloads Today: {downloads}/{max_limit}\n"
        f"🎉 Thank you for using *Velveta Bots*!"
    )

    await message.reply(text, quote=True, parse_mode="markdown")
