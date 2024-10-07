from pyrogram import filters
from pyrogram.client import Client
from pyrogram.types import Message
from os import getenv
import logging
import re
import yt_dlp

BOT_TOKEN = getenv("BOT_TOKEN", "")
API_ID = getenv("API_ID", "")
API_HASH = getenv("API_HASH", "")
DOWNLOAD_PATH = getenv("DL_PATH", "./downloads")
TARGET_CHAT_ID= getenv("TARGET_CHAT_ID", "827128705")

app = Client("banana_yt", bot_token=BOT_TOKEN, api_id=API_ID, api_hash=API_HASH)
yt_opts = {
    # 'verbose': True,
    'username': 'oauth2',
    'password': '',
    'format': "bestvideo[ext=mp4][vcodec!*=av01][vcodec!*=vp09]+bestaudio[ext=m4a]/bestvideo+bestaudio",
    'outtmpl': f'{DOWNLOAD_PATH}/%(title)s.%(ext)s',
}
ydl = yt_dlp.YoutubeDL(yt_opts)

url_pattern = re.compile(
    r'^(https?://)?(www\.)?(youtube\.com/watch\?v=|youtu\.be/)([a-zA-Z0-9_-]{11})',
    # r'(?:(?:http|ftp)s?://)?(?:[a-z0-9-]+\.)+[a-z]{2,6}(?:/[^\s]*)?',
    re.IGNORECASE
)

@app.on_message(filters.command("start"))
async def hello(_, message):
    await message.reply("banana........")

@app.on_message(filters.regex(r'^(https?://)?(www\.)?(youtube\.com/watch\?v=|youtu\.be/)([a-zA-Z0-9_-]{11})'))
async def download_yt(client: Client, message: Message):
    url = message.text
    ydl.download(url)
    filename = ydl.prepare_filename(ydl.extract_info(url))
    await message.reply("download ended")
    await message.reply_video(video=open("./downloads/Firelake - Live To Forget (S.T.A.L.K.E.R.： Зов Припяти OST).mp4", 'rb'))

app.run()
