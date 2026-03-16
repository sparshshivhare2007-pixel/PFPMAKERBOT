from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import ContextTypes

async def theme(update: Update, context: ContextTypes.DEFAULT_TYPE):

    keyboard = [
        [InlineKeyboardButton("Cyber Neon", callback_data="cyber")],
        [InlineKeyboardButton("Fire Rage", callback_data="fire")],
        [InlineKeyboardButton("Neon Green", callback_data="green")],
        [InlineKeyboardButton("Royal Gold", callback_data="gold")],
        [InlineKeyboardButton("Dark Purple", callback_data="purple")],
        [InlineKeyboardButton("Bloody Red", callback_data="red")]
    ]

    await update.message.reply_text(
        "Logo theme chuno:",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )


async def theme_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):

    query = update.callback_query
    await query.answer()

    context.user_data["theme"] = query.data

    await query.edit_message_text(f"Theme set: {query.data}")
