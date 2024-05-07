import os
import datetime
from dotenv import load_dotenv
import telebot

from telebot.storage import StateMemoryStorage
from telebot.handler_backends import State, StatesGroup
from telebot import custom_filters

load_dotenv()

state_storage = StateMemoryStorage()

TOKEN = os.environ.get("TOKEN")
bot = telebot.TeleBot(token=TOKEN, state_storage=state_storage)

class UserInfo(StatesGroup):
    first_name = State()
    last_name = State()
    age = State()

@bot.message_handler(commands=['start'])
def start(m):
    bot.send_message(m.chat.id, 'اسمت چیه؟')
    bot.set_state(m.from_user.id, UserInfo.first_name, m.chat.id)

@bot.message_handler(state=UserInfo.first_name)
def first_name(m):
    bot.send_message(m.chat.id, 'فامیلیت چیه؟')
    bot.set_state(m.from_user.id, UserInfo.last_name, m.chat.id)

    with bot.retrieve_data(m.from_user.id, m.chat.id) as data:
        data['first_name'] = m.text    

@bot.message_handler(state=UserInfo.last_name)
def last_name(m):
    bot.send_message(m.chat.id, 'چند سالته؟')
    bot.set_state(m.from_user.id, UserInfo.age, m.chat.id)

    with bot.retrieve_data(m.from_user.id, m.chat.id) as data:
        data['last_name'] = m.text    

@bot.message_handler(state=UserInfo.age)
def age(m):
    with bot.retrieve_data(m.from_user.id, m.chat.id) as data:
        bot.send_message(m.chat.id, f"اسم شما: {data['first_name']}\nفامیلی شما: {data['last_name']}\nسن شما: {m.text}")

    bot.delete_state(m.from_user.id, m.chat.id)

bot.add_custom_filter(custom_filters.StateFilter(bot))


bot.infinity_polling()
