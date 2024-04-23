import os
from dotenv import load_dotenv
from telegram import Update, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters

load_dotenv()

async def say_hello(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = ReplyKeyboardMarkup([
        [KeyboardButton("Hello"), KeyboardButton("Hello")],
        [KeyboardButton("Bye")]
    ])
    await update.message.reply_text("Keyboard sent:", reply_markup=keyboard)

async def Hello_or_bye( update: Update, context: ContextTypes.DEFAULT_TYPE ):
    if update.message.text == "Hello":
        await update.message.reply_text("How are you?", reply_markup=ReplyKeyboardRemove())
    if update.message.text == "Bye":
        await update.message.reply_text("Goodbye baby.", reply_markup=ReplyKeyboardRemove())
    pass

TOKEN = os.environ.get('TELEGRAM_BOT_TOKEN')

application = ApplicationBuilder().token(TOKEN).build()

application.add_handler( CommandHandler( "start", say_hello ) )
application.add_handler( MessageHandler( filters.ALL, Hello_or_bye ) )

application.run_polling(allowed_updates=Update.ALL_TYPES)