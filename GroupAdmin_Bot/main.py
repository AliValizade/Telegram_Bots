import os
import datetime
from dotenv import load_dotenv
import telebot

load_dotenv()
TOKEN = os.environ.get("TOKEN")
bot = telebot.TeleBot(TOKEN)

"""
Text formatting (parse_mode='HTML')
Bold: <b>your text</b>
Italic: <i>your text</i>
Mono: <code>your text</code>
Endline: <ins>your text</ins>
Stric: <s>your text</s>

Text formatting (parse_mode='MarkdownV2')
Spoiler: ||your text||
Bold: **your text**
Link: [text](link address)
"""

@bot.message_handler(commands=['start'])
def start(m):
    text1 = '<b>این متن بولد است</b>'
    text2 = '<i>این متن ایتالیک است</i>'
    text3 = '<code>این متن مونو است</code>'
    text4 = '<ins>این متن آندرلاین است</ins>'
    text5 = '<s>این متن استریک است</s>'
    text6 = '||این متن اسپویلر است||'
    text7 = '**این متن بولد است**'
    text8 = '[این متن لینک است](https://www.varzesh3.com/)'

    bot.send_message(m.chat.id, text1, parse_mode='HTML')
    bot.send_message(m.chat.id, text2, parse_mode='HTML')
    bot.send_message(m.chat.id, text3, parse_mode='HTML')
    bot.send_message(m.chat.id, text4, parse_mode='HTML')
    bot.send_message(m.chat.id, text5, parse_mode='HTML')
    bot.send_message(m.chat.id, text6, parse_mode='MarkdownV2')
    bot.send_message(m.chat.id, text7, parse_mode='MarkdownV2')
    bot.send_message(m.chat.id, text8, parse_mode='MarkdownV2', disable_web_page_preview=True)


@bot.message_handler(content_types=['new_chat_members'])
def welcome(m):
    bot.reply_to(m, f'کاربر {m.from_user.first_name} به گروه خوش آمدی')

@bot.chat_join_request_handler(func=lambda r:True)
def approve(r):
    bot.approve_chat_join_request(chat_id=r.chat.id, user_id=r.from_user.id )
    text = f'<i>کاربر {r.from_user.first_name} به گروه پیوست.</i>'
    bot.send_message(r.chat.id, text, parse_mode='HTML')

@bot.message_handler(func=lambda m: m.text == 'پین')
def pin(m):
    bot.pin_chat_message(m.chat.id, m.reply_to_message.id)
    bot.reply_to(m, 'پیام موردنظر پین شد')

@bot.message_handler(func=lambda m: m.text == 'افزودن ادمین')
def promote(m):
    bot.promote_chat_member(
        m.chat.id,
        m.reply_to_message.json['from']['id'],
        can_change_info= True,
        can_post_messages= True,
        can_edit_messages= True, 
        can_delete_messages= True, 
        can_invite_users= True, 
        can_restrict_members= True, 
        can_pin_messages= True, 
        can_promote_members= True, 
        can_manage_chat= True, 
        can_manage_video_chats= True, 
        can_manage_voice_chats= True, 
        can_manage_topics= False,
    )

@bot.message_handler(func=lambda m: m.text.startwith('بن'))
def ban(m):
    duration = int(m.text.split()[-1])
    date = datetime.datetime.now() + datetime.timedelta(minutes=duration)
    until_date = int(date.timestamp())
    bot.ban_chat_member(m.chat.id, m.reply_to_message.from_user.id, until_date=until_date)
    bot.reply_to(m, f'کاربر {m.reply_to_message.from_user.id} بن {duration} شد')

@bot.message_handler(func=lambda m: m.text == 'حذف بن')
def ban(m):
    bot.unban_chat_member(m.chat.id, m.reply_to_message.from_user.id)
    bot.reply_to(m, f'کاربر {m.reply_to_message.from_user.id} حذف بن شد')

@bot.message_handler(func=lambda m: m.text == 'کیک بن')
def ban(m):
    bot.kick_chat_member(m.chat.id, m.reply_to_message.from_user.id, until_date=5, revoke_messages=True)
    bot.reply_to(m, f'کاربر {m.reply_to_message.from_user.id} بن موقت شد')

@bot.message_handler(func=lambda m: m.text.startwith('سکوت'))
def restrict(m):
    duration = int(m.text.split()[-1])
    date = datetime.datetime.now() + datetime.timedelta(minutes=duration)
    until_date = int(date.timestamp())
    bot.restrict_chat_member(m.chat.id, m.reply_to_message.from_user.id, until_date=until_date,
                             can_send_messages= False, 
                             can_send_media_messages= False, 
                             can_send_polls= False, 
                             can_send_other_messages= False, 
                             can_add_web_page_previews= False, 
                             can_change_info= False, 
                             can_invite_users= False, 
                             can_pin_messages= False, 
                            )
    bot.reply_to(m, f'کاربر {m.reply_to_message.from_user.id} سکوت شد')


@bot.message_handler(func=lambda m: m.text == 'حذف سکوت')
def derestrict(m):
    bot.restrict_chat_member(m.chat.id, m.reply_to_message.from_user.id, until_date=10,
                             can_send_messages= True, 
                             can_send_media_messages= True, 
                             can_send_polls= True, 
                             can_send_other_messages= True, 
                             can_add_web_page_previews= True, 
                             can_change_info= True, 
                             can_invite_users= True, 
                             can_pin_messages= True, 
                            )
    bot.reply_to(m, f'کاربر {m.reply_to_message.from_user.id} حذف سکوت شد')


bot.infinity_polling()
