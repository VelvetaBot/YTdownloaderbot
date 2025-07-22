from pyrogram import filters
from pyrogram.types import Message

def register(app):
    @app.on_message(filters.command("version"))
    async def version(client, message: Message):
        await message.reply("🤖 Bot Version: `v1.0.0`")
