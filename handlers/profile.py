from pyrogram import filters
from pyrogram.types import Message
from database.users import get_user_data

def register(app):
    @app.on_message(filters.command("profile"))
    async def profile(client, message: Message):
        user = await get_user_data(message.from_user.id)
        if user:
            text = (
                f"📄 **Your Profile**\n\n"
                f"🆔 Unique ID: `{user['_id']}`\n"
                f"👤 Name: {user['first_name']} {user['last_name']}\n"
                f"📦 Downloads today: {user['downloads_today']}/3\n"
                f"🗓️ Added: {user['join_date']}\n\n"
                "⚠️ The bot stores only this basic data."
            )
        else:
            text = "User not found!"
        await message.reply_text(text)

