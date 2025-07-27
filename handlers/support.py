# support.py

from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

@Client.on_message(filters.command(["support", "help"]) & filters.private)
async def support_message(client, message: Message):
    text = (
        "🛠 *Support & Help*\n\n"
        "Having trouble using the bot? Want to report a bug or give feedback?\n\n"
        "Feel free to reach out to our developer!"
    )

    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("💬 Developer", url="https://t.me/Yaswanth_venkata_naga_sai")
            ],
            [
                InlineKeyboardButton("📢 Updates Channel", url="https://t.me/Velvetabots")
            ]
        ]
    )

    await message.reply(text, reply_markup=keyboard, parse_mode="markdown")
