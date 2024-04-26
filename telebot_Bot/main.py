import os
from dotenv import load_dotenv
import telebot

load_dotenv()
TOKEN = os.environ.get("TOKEN")
bot = telebot.TeleBot(TOKEN)

first_button = telebot.types.InlineKeyboardButton('Button 1', url='https://t.me/kia_todo_list_bot')
second_button = telebot.types.InlineKeyboardButton('Button 2', url='https://t.me/kia_todo_list_bot')
markup = telebot.types.InlineKeyboardMarkup()
markup.add(first_button, second_button)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, 'Hi', reply_markup=markup)




bot.infinity_polling()