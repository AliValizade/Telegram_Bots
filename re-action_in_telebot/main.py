import os
from dotenv import load_dotenv
from telebot import TeleBot
from telebot.types import ReactionTypeEmoji
from telebot.util import update_types

load_dotenv()

TOKEN = os.environ.get("TOKEN")
bot = TeleBot(token=TOKEN)

@bot.message_handler(commands=['start'])
def start(m):
    bot.send_message(chat_id=m.chat.id, text='Hello my dear, welcome to my bot.')
    bot.set_message_reaction(chat_id=m.chat.id, message_id=m.message_id, reaction=[ReactionTypeEmoji(emoji='😍')])


@bot.message_reaction_handler()
def reaction(r):
    print(r.chat.first_name, r.chat.last_name)


bot.polling(allowed_updates=update_types)
