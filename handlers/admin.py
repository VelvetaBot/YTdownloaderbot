# admin.py

from pyrogram import Client, filters
from pyrogram.types import Message
from users import reset_user_limit, get_all_users
import datetime

ADMIN_ID = 883128927  # Replace with your Telegram user ID

@Client.on_message(filters.command("reset") & filters.user(ADMIN_ID))
async def reset_limits(client, message: Message):
    reset_user_limit()
    await message.reply("✅ All user download limits have been reset for today.")

@Client.on_message(filters.command("users") & filters.user(ADMIN_ID))
async def user_list(client, message: Message):
    users = get_all_users()
    await message.reply(f"👥 Total Users: {len(users)}")

@Client.on_message(filters.command("broadcast") & filters.user(ADMIN_ID))
async def broadcast(client, message: Message):
    if not message.reply_to_message:
        await message.reply("📢 Reply to a message you want to broadcast.")
        return

    text = message.reply_to_message.text
    users = get_all_users()
    success = 0
    fail = 0

    for user in users:
        try:
            await client.send_message(user["user_id"], text)
            success += 1
        except:
            fail += 1

    await message.reply(f"✅ Broadcast sent!\nSuccess: {success} | Failed: {fail}")
