# main.py
from decouple import config
from telegram import Update
from telegram.ext import ApplicationBuilder, CallbackQueryHandler, CommandHandler, ConversationHandler, MessageHandler, filters

from Controllers.TodoController import TodoController, ADD_TODO_TEXT, CHECK_TODO_NUMBER

TOKEN = config('TOKEN')
application = ApplicationBuilder().token(TOKEN).build()

# Conversation handler for adding new todo with 'per_message=False'
conv_handler = ConversationHandler(
    entry_points=[CommandHandler('add', TodoController.add_todo)],
    states={
        ADD_TODO_TEXT: [MessageHandler(filters.TEXT & ~filters.COMMAND, TodoController.add_todo_text)]
    },
    fallbacks=[CommandHandler('cancel', TodoController.start)],
    per_message=False  # Set 'per_message=False' for text message handling
)

# Conversation handler for checking todo with 'per_message=False'
check_handler = ConversationHandler(
    entry_points=[CommandHandler('check', TodoController.check_todo)],
    states={
        CHECK_TODO_NUMBER: [MessageHandler(filters.TEXT & ~filters.COMMAND, TodoController.check_todo_number)]
    },
    fallbacks=[CommandHandler('cancel', TodoController.start)],
    per_message=False  # Set 'per_message=False' for text message handling
)

# Handle commands through callback queries
application.add_handler(conv_handler)
application.add_handler(check_handler)
application.add_handler(CallbackQueryHandler(TodoController.start, pattern='^start$'))
application.add_handler(CallbackQueryHandler(TodoController.help, pattern='^help$'))
application.add_handler(CallbackQueryHandler(TodoController.list_todos, pattern='^list$'))
application.add_handler(CallbackQueryHandler(TodoController.clear_todos, pattern='^clear$'))

application.run_polling()
