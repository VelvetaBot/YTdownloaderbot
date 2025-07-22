from pyrogram import filters
from pyrogram.types import Message
from database.users import get_user_data

def register(app):
    @app.on_message(filters.command("history"))
    async def history(client, message: Message):
        user = await get_user_data(message.from_user.id)
        if not user or "history" not in user or len(user["history"]) == 0:
            await message.reply("📭 You don’t have any download history yet.")
            return

        history_text = "📥 **Your Download History:**\n\n"
        for i, item in enumerate(reversed(user["history"][-10:]), 1):
            history_text += (
                f"{i}. 🎬 `{item['title']}`\n"
                f"   📦 {item['size']} | 🕒 {item['time']}\n\n"
            )

        await message.reply(history_text)
