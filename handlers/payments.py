# payments.py

from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from users import set_premium_pending, is_premium

@Client.on_message(filters.command("buy") & filters.private)
async def buy_premium(client, message: Message):
    if is_premium(message.from_user.id):
        await message.reply("✅ You already have Premium access!")
        return

    set_premium_pending(message.from_user.id)

    await message.reply(
        "💎 *Upgrade to Velvetta Premium!*\n\n"
        "🚀 Unlimited downloads\n"
        "📲 Access to Instagram Link Downloader\n"
        "⚡ Faster speeds\n"
        "🎁 Offer: ₹49 for 60 days (Regular ₹99)\n\n"
        "📸 After payment, please send the *screenshot of your transaction* here.\n"
        "Your premium will be activated after verification.",
        parse_mode="markdown",
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("📨 Contact Developer", url="https://t.me/Yaswanth_venkata_naga_sai")]
        ])
    )

@Client.on_message(filters.private & filters.photo)
async def handle_screenshot(client, message: Message):
    if not is_premium(message.from_user.id):
        await message.forward(chat_id=883128927)  # Admin ID
        await message.reply(
            "✅ Screenshot received. Please wait while we verify and activate your Premium.\n"
            "⏳ Typically takes a few minutes."
        )
