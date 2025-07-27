# payments.py

from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

@Client.on_message(filters.command("upgrade"))
async def upgrade(client, message: Message):
    text = (
        "💎 *Upgrade to Premium!*\n\n"
        "Unlock all the features:\n"
        "🚀 Unlimited downloads\n"
        "📸 Instagram Link Downloader access\n"
        "⚡ Super-fast speed\n\n"
        "*Offer Price:* ₹49 for 60 days (Regular ₹99)\n\n"
        "📩 After payment, please send a screenshot of the transaction here to activate Premium access.\n"
        "✅ We will verify it manually.\n\n"
        "For help, contact @Yaswanth_venkata_naga_sai"
    )

    keyboard = InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("📩 Contact Support", url="https://t.me/Yaswanth_venkata_naga_sai")],
            # Add payment link button later
        ]
    )

    await message.reply(text, reply_markup=keyboard, parse_mode="markdown", quote=True)
