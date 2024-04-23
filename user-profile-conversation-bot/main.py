import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import ContextTypes, CommandHandler, ApplicationBuilder, MessageHandler, ConversationHandler, filters

from Controllers.UserProfileController import user_profile_controller_conversation_handler

load_dotenv()

TOKEN = os.environ.get('TELEGRAM_BOT_TOKEN')

application = ApplicationBuilder().token(TOKEN).build()
application.add_handler( user_profile_controller_conversation_handler )

application.run_polling(allowed_updates=Update.ALL_TYPES)