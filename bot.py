from telegram.ext import Application, CommandHandler, MessageHandler, CallbackQueryHandler, filters

from config import BOT_TOKEN
from handlers.start import start
from handlers.pfp import create_pfp
from handlers.logo import create_logo
from handlers.theme import theme, theme_callback

app = Application.builder().token(BOT_TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("logo", create_logo))
app.add_handler(CommandHandler("theme", theme))

app.add_handler(CallbackQueryHandler(theme_callback))

app.add_handler(MessageHandler(filters.PHOTO, create_pfp))

print("BOT STARTED")

app.run_polling()
