from decouple import config
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler

from Controllers.TodoController import TodoController

TOKEN = config('TOKEN')
application = ApplicationBuilder().token(TOKEN).build()

application.add_handler(CommandHandler('add', TodoController.add_todo))
application.add_handler(CommandHandler('list', TodoController.list_todos))
application.add_handler(CommandHandler('check', TodoController.check_todo))
application.add_handler(CommandHandler('clear', TodoController.clear_todos))


application.run_polling(allowed_updates=Update.ALL_TYPES)
