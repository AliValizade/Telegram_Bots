from telegram import Update
from telegram.ext import ContextTypes

from Models.Todo import Todo
from Models.TodoList import todo_list

class TodoController:
    @staticmethod
    async def add_todo(update:Update, context: ContextTypes.DEFAULT_TYPE):
        command = update.message.text.split()[0]
        title = " ".join(update.message.text.split(command)[1:] )
        todo_list.append(Todo(title))
        await update.message.reply_text('Added note!')

    @staticmethod
    async def list_todos(update:Update, context: ContextTypes.DEFAULT_TYPE):
        if len(todo_list) == 0:
            await update.message.reply_text('There are no tasks to do!')
            return 
        answer = ""
        for i, todo in enumerate(todo_list):
            answer = answer + f"{i + 1} - {'✅' if todo.is_completed else '⭕'} {todo.title}\n"
        await update.message.reply_text(answer)

    @staticmethod
    async def check_todo(update:Update, context:ContextTypes.DEFAULT_TYPE):
        index = int(context.args[0])
        if index > len(todo_list) or index <= 0:
            await update.message.reply_text('ERROR: The task no exist.')
            return
        todo_list[index - 1].set_completed()
        await update.message.reply_text(f'The task {index} done.')
