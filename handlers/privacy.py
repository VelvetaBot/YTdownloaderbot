from pyrogram import filters
from pyrogram.types import Message

def register(app):
    @app.on_message(filters.command("privacy"))
    async def privacy(client, message: Message):
        await message.reply(
            "🔒 **Privacy Policy**\n\n"
            "This bot stores only your Telegram ID and download stats.\n"
            "We do not collect personal data, passwords, or payment info."
        )
