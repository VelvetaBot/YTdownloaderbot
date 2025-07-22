from pyrogram import filters
from pyrogram.types import Message

def register(app):
    @app.on_message(filters.command("support"))
    async def support(client, message: Message):
        await message.reply("📩 Contact support: @your_support_username")
