from decouple import config
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler

from Controllers.TodoController import TodoController

TOKEN = config('TOKEN')
application = ApplicationBuilder().token(TOKEN).build()

application.add_handler(CommandHandler('add', TodoController.add_todo))


application.run_polling(allowed_updates=Update.ALL_TYPES)
