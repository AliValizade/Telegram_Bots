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

@bot.message_handler(func=lambda m: m.text == 'بن')
def ban(m):
    bot.ban_chat_member(m.chat.id, m.reply_to_message.from_user.id)
    bot.reply_to(m, f'کاربر {m.reply_to_message.from_user.id} بن شد')

@bot.message_handler(func=lambda m: m.text == 'حذف بن')
def ban(m):
    bot.unban_chat_member(m.chat.id, m.reply_to_message.from_user.id)
    bot.reply_to(m, f'کاربر {m.reply_to_message.from_user.id} حذف بن شد')

@bot.message_handler(func=lambda m: m.text == 'کیک بن')
def ban(m):
    bot.kick_chat_member(m.chat.id, m.reply_to_message.from_user.id, until_date=5, revoke_messages=True)
    bot.reply_to(m, f'کاربر {m.reply_to_message.from_user.id} بن موقت شد')

@bot.message_handler(func=lambda m: m.text == 'سکوت')
def restrict(m):
    bot.restrict_chat_member(m.chat.id, m.reply_to_message.from_user.id, until_date=10,
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
