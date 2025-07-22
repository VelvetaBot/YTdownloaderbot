from pyrogram import filters
from pyrogram.types import Message

def register(app):
    @app.on_message(filters.command("pay"))
    async def pay(client, message: Message):
        await message.reply(
            "💳 **Payment Options**\n\n"
            "You can upgrade your plan via UPI:\n\n"
            "📌 UPI ID: `yourupi@bank`\n"
            "💰 Plan: ₹29 - Unlimited for 30 days\n\n"
            "After payment, send the screenshot to @your_support_username."
        )

    @app.on_message(filters.command("pay_history"))
    async def pay_history(client, message: Message):
        # For now, static text (no DB yet)
        await message.reply("📜 You haven’t made any payments yet.")

