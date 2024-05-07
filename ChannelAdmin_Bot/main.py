import os
import datetime
from dotenv import load_dotenv
import telebot
from telebot import types

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


# Inline Query
items = [
    {'id':'1', 'title':'Todolist_bot', 'description':'ربات برنامه ریزی روزانه\nاگه میخوای کارای روزانه ات رو برنامه ریزی کنی بیا اینجا', 'thumb':'https://imgurl.ir/download.php?file=b771194_650.jpg', 'message':'ربات تلگرام TodoList'},
    {'id':'2', 'title':'Agahi7/24', 'description':'ربات برنامه ریزی روزانه\nاگه میخوای کارای روزانه ات رو برنامه ریزی کنی بیا اینجا', 'thumb':'https://imgurl.ir/download.php?file=p74120_ali.jpg', 'message':'ربات تلگرام TodoList'},
    {'id':'3', 'title':'Remote_Ads', 'description':'ربات برنامه ریزی روزانه\nاگه میخوای کارای روزانه ات رو برنامه ریزی کنی بیا اینجا', 'thumb':'https://imgurl.ir/download.php?file=g88280_Capture1.jpg', 'message':'ربات تلگرام TodoList'},
    {'id':'4', 'title':'Test_bot', 'description':'ربات برنامه ریزی روزانه\nاگه میخوای کارای روزانه ات رو برنامه ریزی کنی بیا اینجا', 'thumb':'https://imgurl.ir/download.php?file=i29182_img17.jpg', 'message':'ربات تلگرام TodoList'},
]

@bot.inline_handler(lambda query: len(query.query) == 0)
def handle_inline_query(query):
    results = []
    for item in items:
        result = types.InlineQueryResultArticle(
            id=item['id'],
            title=item['title'],
            description=item['description'],
            input_message_content=types.InputTextMessageContent(
                message_text=item['message']
            ),
            thumbnail_url=item['thumb']
        )
        results.append(result)
    
    bot.answer_inline_query(query.id, results)



bot.infinity_polling()
