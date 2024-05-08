import os
from dotenv import load_dotenv
from telebot import TeleBot
from telebot.types import ReactionTypeEmoji, ReplyParameters, LinkPreviewOptions
from telebot.util import update_types

load_dotenv()

TOKEN = os.environ.get("TOKEN")
bot = TeleBot(token=TOKEN)

# Re-action to command and send message
@bot.message_handler(commands=['start1'])
def start1(m):
    bot.send_message(chat_id=m.chat.id, text='Hello my dear, welcome to my bot.')
    bot.set_message_reaction(chat_id=m.chat.id, message_id=m.message_id, reaction=[ReactionTypeEmoji(emoji='😍')])

# Reply to message in another chat
@bot.message_handler(commands=['start2'])
def start2(m):
    bot.send_message(chat_id=-1002035951847, text='Hello my dear.', reply_parameters=ReplyParameters(message_id=m.message_id, chat_id=m.chat.id))


# Customize link preview
@bot.message_handler(commands=['start3'])
def start3(m):
    bot.send_message(
        chat_id=m.chat.id, 
        text='Hello my dear.\n\nhttps://t.me/Remote_project_bot', 
        link_preview_options=LinkPreviewOptions(
            is_disabled=False,
            url='https://t.me/kia_todo_list_bot',
            prefer_large_media=True,
            show_above_text=True
        )
    )
    

# Forward multiple messages together
@bot.message_handler(commands=['start4'])
def start4(m):
    bot.forward_messages(chat_id=m.chat.id,from_chat_id='@remote_ad', message_ids=[11, 13])



@bot.message_reaction_handler()
def reaction(r):
    print(r.chat.first_name, r.chat.last_name)


bot.polling(allowed_updates=update_types)
