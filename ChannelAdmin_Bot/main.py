import os
import datetime
from dotenv import load_dotenv
import telebot

load_dotenv()
TOKEN = os.environ.get("TOKEN")
bot = telebot.TeleBot(TOKEN)


# Channel admin 
@bot.channel_post_handler(content_types=['text', 'audio', 'video', 'document', 'sticker', 'photo', 'voice', 'contact', 'location', 'venue', 'pinnedmessage'])
def forwardingg(m):
    test1 = -1002111355264
    test2 = -1002050675510
    # forward
    bot.forward_message(chat_id=test2, from_chat_id=test1, message_id=m.message_id, protect_content=True)
    # copy
    bot.copy_message(chat_id=test2, from_chat_id=test1, message_id=m.message_id)




bot.infinity_polling()
