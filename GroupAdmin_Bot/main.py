import os
import time
from dotenv import load_dotenv
import telebot
from telebot import types

load_dotenv()
TOKEN = os.environ.get("TOKEN")
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(content_types=['new_chat_members'])
def welcome(m):
    bot.reply_to(m, f'کاربر {m.from_user.first_name} به گروه خوش آمدی')

@bot.chat_join_request_handler(func=lambda r:True)
def approve(r):
    bot.approve_chat_join_request(chat_id=r.chat.id, user_id=r.from_user.id )
    bot.send_message(r.chat.id, f'کاربر {r.from_user.first_name} به گروه پیوست.')

@bot.message_handler(func=lambda m: m.text == 'پین')
def pin(m):
    bot.pin_chat_message(m.chat.id, m.reply_to_message.id)
    bot.reply_to(m, 'پیام موردنظر پین شد')



bot.infinity_polling()
