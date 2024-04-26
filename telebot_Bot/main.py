import os
from dotenv import load_dotenv
import telebot

load_dotenv()
TOKEN = os.environ.get("TOKEN")
bot = telebot.TeleBot(TOKEN)

# Inline Button
first_button = telebot.types.InlineKeyboardButton('Button 1', url='https://t.me/kia_todo_list_bot')
second_button = telebot.types.InlineKeyboardButton('Button 2', callback_data='Hi')
third_button = telebot.types.InlineKeyboardButton('Button 3', callback_data='Bye')
markup = telebot.types.InlineKeyboardMarkup()
markup.add(first_button, second_button, third_button)

# Keyboaed
key_markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
key_markup.add('Register', 'Two', 'Three')


@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    if call.data == 'Hi':
        # bot.send_message(call.message.chat.id, 'You clicked on Hi button.')
        bot.answer_callback_query(call.id, 'You clicked on Hi button.', show_alert=True)
        # bot.reply_to(call.message, 'You clicked on Hi button.')
    elif call.data == 'Bye':
        bot.answer_callback_query(call.id, 'You clicked on Bye button.')
    

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, 'Hi', reply_markup=markup)


@bot.message_handler(commands=['help'])
def help_me(message):
    bot.reply_to(message, 'What can I do?', reply_markup=key_markup)


@bot.message_handler(func=lambda m: True)
def info(message):
    if message.text == 'Register':
        msg = bot.send_message(message.chat.id, 'Please enter your Name:')
        bot.register_next_step_handler(msg, name)

def name(message):
    global nm
    nm = message.text
    msg = bot.send_message(message.chat.id, 'Enter your Age:')
    bot.register_next_step_handler(msg, age)

def age(message):
    global ag
    ag = message.text
    msg = bot.send_message(message.chat.id, 'How tall are you?')
    bot.register_next_step_handler(msg, tall)

def tall(message):
    tal = message.text
    msg = bot.send_message(message.chat.id, f'Your name: {nm}\nAge: {ag}\nTall: {tal}')


bot.infinity_polling()