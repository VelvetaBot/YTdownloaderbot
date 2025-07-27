# history.py

from pyrogram import Client, filters
from pyrogram.types import Message

# Temporary in-memory history store (clears when bot restarts)
user_history = {}

@Client.on_message(filters.command("history"))
async def show_history(client, message: Message):
    user_id = message.from_user.id
    history = user_history.get(user_id, [])

    if not history:
        await message.reply("📭 You have no download history yet.")
        return

    text = "📚 *Your Download History:*\n\n"
    for i, item in enumerate(history[-10:], 1):  # Show last 10 items
        text += f"{i}. {item}\n"

    await message.reply(text, parse_mode="markdown")

# Use this to add a download to the user's history
def add_to_history(user_id: int, video_title: str):
    if user_id not in user_history:
        user_history[user_id] = []
    user_history[user_id].append(video_title)
