from telegram import Update
from telegram.ext import ContextTypes

from PIL import Image, ImageDraw, ImageFont, ImageFilter
from io import BytesIO
import requests


async def create_pfp(update: Update, context: ContextTypes.DEFAULT_TYPE):

    photo = update.message.photo[-1]

    name = update.message.caption or "GAMER"

    file = await context.bot.get_file(photo.file_id)

    img_bytes = requests.get(file.file_path).content

    img = Image.open(BytesIO(img_bytes)).convert("RGB")

    img = img.resize((1024,1024))

    bw = img.convert("L").convert("RGB")

    draw = ImageDraw.Draw(bw)

    font = ImageFont.truetype("arial.ttf",120)

    w,h = draw.textsize(name,font)

    x = (1024-w)//2
    y = 850

    draw.text((x,y),name,(255,0,255),font)

    glow = bw.filter(ImageFilter.GaussianBlur(10))

    final = Image.blend(glow,bw,0.7)

    bio = BytesIO()

    bio.name="pfp.png"

    final.save(bio,"PNG")

    bio.seek(0)

    await update.message.reply_photo(bio)
