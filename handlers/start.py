# plugins/start.py

from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from users import get_user_data, update_user_data
from datetime import datetime

# Constants
DAILY_LIMIT = 5
CHANNEL_URL = "https://t.me/Velvetabots"

@Client.on_message(filters.command("start"))
async def start_command(client, message):
    user_id = message.from_user.id
    user_data = get_user_data(user_id)

    today = datetime.today().strftime('%Y-%m-%d')
    if user_data is None:
        update_user_data(user_id, 0, today)
        user_data = {"downloads": 0, "last_download_date": today}

    elif user_data["last_download_date"] != today:
        update_user_data(user_id, 0, today)
        user_data["downloads"] = 0

    if user_data["downloads"] < DAILY_LIMIT:
        await message.reply_text(
            "🎀 *Welcome* 🎀 to the Velvetta YouTube Downloader Bot!\n"
            "Ready to start downloading? Just subscribe to our channel, and you'll be all set! 🎉",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("📢 Subscribe Channel", url=CHANNEL_URL)],
                [InlineKeyboardButton("👤 Profile", callback_data="profile"),
                 InlineKeyboardButton("🛠 Support", url="https://t.me/Yaswanth_venkata_naga_sai")]
            ]),
            parse_mode="markdown"
        )
    else:
        await message.reply_text(
            "Oh no! 😔 You've reached your daily download limit for today.\n\n"
            "Don't let anything stop your downloads! ✨ Go Premium now for:\n\n"
            " * 🚀 Unlimited downloads\n"
            " * 🔗 Exclusive Instagram Link Downloader access\n"
            " * ⚡ Blazing-fast speeds and more!\n\n"
            "Get unlimited benefits at a super cheap rate – upgrade today!\n\n"
            "_Please send a screenshot of your transaction to this bot after payment._",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("💳 Payment Options", callback_data="payment_info")],
                [InlineKeyboardButton("🛠 Support", url="https://t.me/Yaswanth_venkata_naga_sai")]
            ]),
            parse_mode="markdown"
        )
