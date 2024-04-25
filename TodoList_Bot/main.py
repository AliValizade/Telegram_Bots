from decouple import config
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ConversationHandler, MessageHandler, filters

from Controllers.TodoController import TodoController, ADD_TODO_TEXT, CHECK_TODO_NUMBER


TOKEN = config('TOKEN')
application = ApplicationBuilder().token(TOKEN).build()

# Add conversation handler for adding todos
conv_handler = ConversationHandler(
    entry_points=[CommandHandler('add', TodoController.add_todo)],
    states={
        ADD_TODO_TEXT: [MessageHandler(filters.TEXT & ~filters.COMMAND, TodoController.add_todo_text)]
    },
    fallbacks=[CommandHandler('cancel', TodoController.start)]
)

check_handler = ConversationHandler(
    entry_points=[CommandHandler('check', TodoController.check_todo)],
    states={
        CHECK_TODO_NUMBER: [MessageHandler(filters.TEXT & ~filters.COMMAND, TodoController.check_todo_number)]
    },
    fallbacks=[CommandHandler('cancel', TodoController.start)]
)

application.add_handler(conv_handler)
application.add_handler(check_handler)
application.add_handler(CommandHandler('start', TodoController.start))
application.add_handler(CommandHandler('help', TodoController.help))
application.add_handler(CommandHandler('list', TodoController.list_todos))
application.add_handler(CommandHandler('clear', TodoController.clear_todos))


application.run_polling(allowed_updates=Update.ALL_TYPES)
