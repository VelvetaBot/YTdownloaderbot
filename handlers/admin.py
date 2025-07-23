from pyrogram import filters
from pyrogram.types import Message
from config import ADMIN_ID
from database.users import ban_user, unban_user, make_premium, count_users

def register(app):
    @app.on_message(filters.command("admin") & filters.user(ADMIN_ID))
    async def admin_menu(client, message: Message):
        await message.reply(
            "🛠️ **Admin Panel**\n\n"
            "/users - Total users\n"
            "/makepremium <user_id> - Upgrade user\n"
            "/ban <user_id> - Ban user\n"
            "/unban <user_id> - Unban user"
        )

    @app.on_message(filters.command("users") & filters.user(ADMIN_ID))
    async def total_users(client, message: Message):
        total = await count_users()
        await message.reply(f"👥 Total users: {total}")

    @app.on_message(filters.command("makepremium") & filters.user(ADMIN_ID))
    async def make_premium_cmd(client, message: Message):
        try:
            user_id = int(message.text.split()[1])
            await make_premium(user_id)
            await message.reply(f"✅ User `{user_id}` is now Premium.")
        except:
            await message.reply("❌ Usage: /makepremium <user_id>")

    @app.on_message(filters.command("ban") & filters.user(ADMIN_ID))
    async def ban_cmd(client, message: Message):
        try:
            user_id = int(message.text.split()[1])
            await ban_user(user_id)
            await message.reply(f"🚫 User `{user_id}` has been banned.")
        except:
            await message.reply("❌ Usage: /ban <user_id>")

    @app.on_message(filters.command("unban") & filters.user(ADMIN_ID))
    async def unban_cmd(client, message: Message):
        try:
            user_id = int(message.text.split()[1])
            await unban_user(user_id)
            await message.reply(f"✅ User `{user_id}` has been unbanned.")
        except:
            await message.reply("❌ Usage: /unban <user_id>")
