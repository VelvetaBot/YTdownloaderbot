from pyrogram import Client, filters
from config import API_ID, API_HASH, BOT_TOKEN
import subprocess

app = Client("yt_bot", api_id=11253846, api_hash=8db4eb50f557faa9a5756e64fb74a51a, bot_token=7523588106:AAHLLbwPCLJwZdKUVL6gA6KNAR_86eHJCWU)

@app.on_message(filters.command("start"))
async def start(client, message):
    await message.reply("👋 Welcome! Send me a YouTube URL to download.")

@app.on_message(filters.text & ~filters.command(["start"]))
async def download_video(client, message):
    url = message.text.strip()
    await message.reply("📥 Downloading... Please wait.")
    try:
        subprocess.run(["yt-dlp", "-f", "best", url, "-o", "video.%(ext)s"], check=True)
        for file in os.listdir("."):
            if file.startswith("video."):
                await message.reply_document(file)
                os.remove(file)
    except Exception as e:
        await message.reply(f"❌ Error: {e}")

app.run()
