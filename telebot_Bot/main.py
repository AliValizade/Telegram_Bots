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

key_markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
key_markup.add('One', 'Two', 'Three')


@bot.message_handler(commands=['help'])
def help_me(message):
    bot.reply_to(message, 'What can I do?', reply_markup=key_markup)

@bot.message_handler()
def keyboard(message):
    if message.text == 'One':
        bot.send_message(message.chat.id, 'You tapped on One button.')
    elif message.text == 'Two':
        bot.send_message(message.chat.id, 'You tapped on Two button.')
    elif message.text == 'Three':
        bot.send_message(message.chat.id, 'You tapped on Three button.')


bot.infinity_polling()