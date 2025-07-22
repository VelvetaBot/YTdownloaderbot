from pyrogram import filters
from pyrogram.types import Message
from database.users import add_user

def register(app):
    @app.on_message(filters.command("start"))
    async def start(client, message: Message):
        await add_user(message.from_user)
        await message.reply_text(
            f"👋 Hello **{message.from_user.first_name}**!\n\n"
            "Send me a YouTube link to get started.\n"
            "Use /profile to see your usage."
        )

