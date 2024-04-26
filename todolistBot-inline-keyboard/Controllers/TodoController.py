from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardRemove, Update
from telegram.ext import CallbackQueryHandler, CallbackContext, ConversationHandler, CommandHandler, MessageHandler, filters
from Models.Todo import Todo
from Models.TodoList import user_todo_lists

# State definitions for the conversation
ADD_TODO_TEXT = range(1)
CHECK_TODO, CHECK_TODO_NUMBER = range(2)

# Define keyboard with InlineKeyboardButton
keyboard = InlineKeyboardMarkup([
    [InlineKeyboardButton("اضافه کردن تسک جدید", callback_data='add'),
     InlineKeyboardButton("لیست تسک‌ها", callback_data='list')],
    [InlineKeyboardButton("علامت زدن تسک به عنوان انجام شده", callback_data='check'),
     InlineKeyboardButton("پاک کردن همه تسک‌ها", callback_data='clear')],
    [InlineKeyboardButton("راهنما", callback_data='help')]
])

class TodoController:
    @staticmethod
    async def start(update: Update, context: CallbackContext):
        query = update.callback_query
        await query.answer()
        user_id = query.from_user.id
        if user_id not in user_todo_lists:
            user_todo_lists[user_id] = []
        await query.message.reply_text('Welcome to TODOList bot, Please use the commands below.', reply_markup=keyboard)

    @staticmethod
    async def help(update: Update, context: CallbackContext):
        query = update.callback_query
        await query.answer()
        await query.message.reply_text(
            'Commands:\n'
            '/add - اضافه کردن تسک جدید\n'
            '/list - لیست تسک‌ها\n'
            '/check - علامت زدن تسک به عنوان انجام شده\n'
            '/clear - پاک کردن همه تسک‌ها',
            reply_markup=keyboard
        )

    @staticmethod
    async def add_todo(update: Update, context: CallbackContext):
        # بررسی کنید که آیا update یک پیام است
        if update.message:
            user_id = update.message.from_user.id
            if user_id not in user_todo_lists:
                user_todo_lists[user_id] = []
            await update.message.reply_text('لطفا تسکی که می‌خواهید اضافه کنید را بنویسید.', reply_markup=ReplyKeyboardRemove())
            return ADD_TODO_TEXT
        else:
            # اگر update یک کوئری بازخورد است، آن را به صورت مناسب رسیدگی کنید
            query = update.callback_query
            await query.answer()
            user_id = query.from_user.id
            if user_id not in user_todo_lists:
                user_todo_lists[user_id] = []
            await query.message.reply_text('لطفا تسکی که می‌خواهید اضافه کنید را بنویسید.', reply_markup=ReplyKeyboardRemove())
            return ADD_TODO_TEXT

    @staticmethod
    async def add_todo_text(update: Update, context: CallbackContext):
        user_id = update.message.from_user.id
        title = update.message.text
        if user_id not in user_todo_lists:
            user_todo_lists[user_id] = []  # Initialize an empty list if not exists
        user_todo_lists[user_id].append(Todo(title))
        await update.message.reply_text('تسک اضافه شد!', reply_markup=keyboard)
        return ConversationHandler.END

    @staticmethod
    async def list_todos(update:Update, context: CallbackContext):
        query = update.callback_query
        await query.answer()
        user_id = query.from_user.id
        if user_id not in user_todo_lists or len(user_todo_lists[user_id]) == 0:
            await update.message.reply_text('There are no tasks to do!', reply_markup=keyboard)
            return
        answer = ""
        for i, todo in enumerate(user_todo_lists[user_id]):
            answer = answer + f"{i + 1} - {'✅' if todo.is_completed else '⭕'} {todo.title}\n"
        await query.message.reply_text(answer, reply_markup=keyboard)

    @staticmethod
    async def check_todo(update:Update, context: CallbackContext):
        query = update.callback_query
        await query.answer()
        await query.message.reply_text('Please send the task number:', reply_markup=ReplyKeyboardRemove())
        return CHECK_TODO_NUMBER

    @staticmethod
    async def check_todo_number(update:Update, context:CallbackContext):
        query = update.callback_query
        await query.answer()
        user_id = query.from_user.id
        try:
            index = int(update.message.text)
        except ValueError:
            await query.message.reply_text('ERROR: Please send a valid task number.', reply_markup=keyboard)
            return CHECK_TODO
        
        if index > len(user_todo_lists[user_id]) or index <= 0:
            await query.message.reply_text('ERROR: The task no exist.', reply_markup=keyboard)
            return CHECK_TODO
        
        user_todo_lists[user_id][index - 1].set_completed()
        await query.message.reply_text(f'The task {index} is now marked as done.')
        await TodoController.list_todos(update, context)
        return ConversationHandler.END

    @staticmethod
    async def clear_todos(update: Update, context: CallbackContext):
        query = update.callback_query
        await query.answer()
        user_id = query.from_user.id
        user_todo_lists[user_id].clear()
        await query.message.reply_text('All tasks removed!', reply_markup=keyboard)


