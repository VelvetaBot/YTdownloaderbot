from pyrogram import filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from database.users import set_language

def register(app):
    @app.on_message(filters.command("language"))
    async def language(client, message: Message):
        keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton("English", callback_data="lang|en")],
            [InlineKeyboardButton("हिंदी", callback_data="lang|hi")],
            [InlineKeyboardButton("తెలుగు", callback_data="lang|te")]
        ])
        await message.reply("🌐 Choose your language:", reply_markup=keyboard)

    @app.on_callback_query()
    async def handle_lang_select(client, query):
        if query.data.startswith("lang|"):
            code = query.data.split("|")[1]
            await set_language(query.from_user.id, code)
            from languages import en, hi, te
            langs = {"en": en.lang, "hi": hi.lang, "te": te.lang}
            await query.message.edit_text(langs[code]["language_selected"])
