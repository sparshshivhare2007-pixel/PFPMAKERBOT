from telegram import Update
from telegram.ext import ContextTypes

TEXT = """
🎮 Gaming PFP & Logo Bot

Gaming PFP:
• Apni photo bhejo
• Caption me naam likho

Example:
Photo + caption:
SPARSH

Logo:
/logo YourText

Theme:
/theme
"""

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(TEXT)
