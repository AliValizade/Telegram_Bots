from telegram import Update, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import ContextTypes, CallbackContext, ConversationHandler, MessageHandler, filters

from Models.Todo import Todo
from Models.TodoList import user_todo_lists


# Define keyboard buttons
keyboard = ReplyKeyboardMarkup([
        [KeyboardButton("/add"), KeyboardButton("/list"), KeyboardButton("/check"), KeyboardButton("/clear")],
        [KeyboardButton("/help")]
    ], resize_keyboard=True)

# Define states for conversation
ADD_TODO, ADD_TODO_TEXT = range(2)
CHECK_TODO, CHECK_TODO_NUMBER = range(2)

class TodoController:
    @staticmethod
    async def start(update:Update, context: ContextTypes.DEFAULT_TYPE):
        user_id = update.message.from_user.id
        if user_id not in user_todo_lists:
            user_todo_lists[user_id] = []
        await update.message.reply_text('Welcome to TODOList bot, Please send /help command to help you.', reply_markup=keyboard)

    @staticmethod
    async def help(update:Update, context: ContextTypes.DEFAULT_TYPE):
        await update.message.reply_text('/add, to add your task.\n/list, to view tasks list.\n/check (i), to check the task(i) as done.\n/clear , to delete all tasks.', reply_markup=keyboard)

    @staticmethod
    async def add_todo(update:Update, context: ContextTypes.DEFAULT_TYPE):
        await update.message.reply_text('Please send the task you want to add.', reply_markup=ReplyKeyboardRemove())
        return ADD_TODO_TEXT
    
    @staticmethod
    async def add_todo_text(update: Update, context: ContextTypes.DEFAULT_TYPE):
        user_id = update.message.from_user.id
        title = update.message.text
        # Ensure the user's todo list is initialized before appending
        if user_id not in user_todo_lists:
            user_todo_lists[user_id] = []  # Initialize an empty list

        user_todo_lists[user_id].append(Todo(title))
        await update.message.reply_text('Added task!', reply_markup=keyboard)
        return ConversationHandler.END

    @staticmethod
    async def list_todos(update:Update, context: ContextTypes.DEFAULT_TYPE):
        user_id = update.message.from_user.id
        if user_id not in user_todo_lists or len(user_todo_lists[user_id]) == 0:
            await update.message.reply_text('There are no tasks to do!', reply_markup=keyboard)
            return
        answer = ""
        for i, todo in enumerate(user_todo_lists[user_id]):
            answer = answer + f"{i + 1} - {'✅' if todo.is_completed else '⭕'} {todo.title}\n"
        await update.message.reply_text(answer, reply_markup=keyboard)

    @staticmethod
    async def check_todo(update:Update, context: ContextTypes.DEFAULT_TYPE):
        await update.message.reply_text('Please send the task number:', reply_markup=ReplyKeyboardRemove())
        return CHECK_TODO_NUMBER

    @staticmethod
    async def check_todo_number(update:Update, context:ContextTypes.DEFAULT_TYPE):
        user_id = update.message.from_user.id
        try:
            index = int(update.message.text)
        except ValueError:
            await update.message.reply_text('ERROR: Please send a valid task number.', reply_markup=keyboard)
            return CHECK_TODO
        
        if index > len(user_todo_lists[user_id]) or index <= 0:
            await update.message.reply_text('ERROR: The task no exist.', reply_markup=keyboard)
            return CHECK_TODO
        
        user_todo_lists[user_id][index - 1].set_completed()
        await update.message.reply_text(f'The task {index} is now marked as done.')
        await TodoController.list_todos(update, context)
        return ConversationHandler.END

    @staticmethod
    async def clear_todos(update: Update, context: ContextTypes.DEFAULT_TYPE):
        user_id = update.message.from_user.id
        user_todo_lists[user_id].clear()
        await update.message.reply_text('All tasks removed!', reply_markup=keyboard)
