from telegram import Update
from telegram.ext import ContextTypes

from PIL import Image, ImageDraw, ImageFont
from io import BytesIO

async def create_logo(update: Update, context: ContextTypes.DEFAULT_TYPE):

    text = " ".join(context.args)

    if not text:
        await update.message.reply_text("Use: /logo YOURTEXT")
        return

    img = Image.new("RGB",(1024,512),(0,0,0))
    draw = ImageDraw.Draw(img)

    font = ImageFont.truetype("arial.ttf",140)

    draw.text((100,200),text,(0,255,255),font=font)

    bio = BytesIO()
    bio.name="logo.png"

    img.save(bio,"PNG")
    bio.seek(0)

    await update.message.reply_photo(bio)
