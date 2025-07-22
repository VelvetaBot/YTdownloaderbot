from pyrogram import Client
from config import API_ID, API_HASH, BOT_TOKEN
import handlers.start
import handlers.profile
import handlers.download

app = Client("yt_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# Import handlers so they register
handlers.start.register(app)
handlers.profile.register(app)
handlers.download.register(app)

print("Bot is running...")
app.run()

