import os
import time
from dotenv import load_dotenv
import telebot
from telebot import types

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
    bot.send_chat_action(message.chat.id, action='typing') # action= 'upload_video' & 'upload_photo' & 'upload_audio' & 'record_video' & 'recordd_audio'
    time.sleep(2)
    bot.send_message(message.chat.id, 'سلام، به ربات ما خوش آمدید.', reply_markup=markup)


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
    bot.send_message(message.chat.id, f'Your name: {nm}\nAge: {ag}\nTall: {tal}')

@bot.message_handler(commands=['get'])
def get_number(m):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    button = types.KeyboardButton(text='ارسال شماره', request_contact=True) # request_location & request_poll exist too.
    markup.add(button)
    bot.send_message(m.chat.id, 'لطفا شماره خود را ارسال کنید:', reply_markup=markup)

@bot.message_handler(content_types=['contact']) # content_types = 'photo' & 'text' & 'video' & 'audio' & 'document' & 'location'
def contact(m):
    print(m.contact)

@bot.message_handler(commands=['pic'])  
def send_pic(message):
    bot.send_chat_action(message.chat.id, action='upload_photo') # action= 'upload_video' & 'upload_photo' & 'upload_audio' & 'record_video' & 'recordd_audio'
    time.sleep(2)
    bot.send_photo(message.chat.id, open('data/ali.jpg', 'rb'), caption='متن اولیه')
    # bot.send_video(message.chat.id, open('data/ali.mp4', 'rb'))
    # bot.send_document(message.chat.id, open('data/requirements.txt', 'r'))
    # bot.send_audio(message.chat.id, open('data/ali.mp3', 'rb'))

media = []
@bot.message_handler(commands=['photos'])  
def send_medias(message):
    p1 = types.InputMediaPhoto(open('data/ali.jpg', 'rb'))
    p2 = types.InputMediaPhoto(open('data/650.JPG', 'rb'))
    media.append(p1)
    media.append(p2)
    bot.send_chat_action(message.chat.id, action='upload_photo') # action= 'upload_video' & 'upload_photo' & 'upload_audio' & 'record_video' & 'recordd_audio'
    time.sleep(2)
    bot.send_media_group(message.chat.id, media=media)


@bot.message_handler(commands=['edittext'])  
def send_photo(message):
    bot.send_chat_action(message.chat.id, action='typing') # action= 'upload_video' & 'upload_photo' & 'upload_audio' & 'record_video' & 'recordd_audio'
    time.sleep(2)
    m = bot.send_message(message.chat.id, 'این متن اولیه است')
    time.sleep(3)
    bot.edit_message_text(chat_id=message.chat.id, message_id=m.message_id, text='متن ادیت شد')


first_photo = open('data/ali.jpg', 'rb')
second_photo = open('data/650.JPG', 'rb')

@bot.message_handler(commands=['editcaption'])
def send_photo(message):
    bot.send_chat_action(message.chat.id, action='upload_photo') # action= 'upload_video' & 'upload_photo' & 'upload_audio' & 'record_video' & 'recordd_audio'
    time.sleep(2)
    m = bot.send_photo(message.chat.id, photo=first_photo, caption='متن اولیه')
    time.sleep(3)
    bot.edit_message_caption(chat_id=message.chat.id, message_id=m.message_id, caption='edited')

@bot.message_handler(commands=['editphoto'])
def send_photo(message):
    bot.send_chat_action(message.chat.id, action='upload_photo') # action= 'upload_video' & 'upload_photo' & 'upload_audio' & 'record_video' & 'recordd_audio'
    m = bot.send_photo(message.chat.id, photo=first_photo, caption='متن اولیه')
    time.sleep(3)
    bot.edit_message_media(chat_id=message.chat.id, message_id=m.message_id,media=types.InputMediaPhoto(second_photo, caption='عکس ویرایش شد'))


key1 = types.InlineKeyboardMarkup()
btn1 = types.InlineKeyboardButton('دکمه 1', callback_data='btn1')
key1.add(btn1)

@bot.message_handler(commands=['editbtn'])
def send_photo(message):
    bot.send_chat_action(message.chat.id, action='upload_photo') # action= 'upload_video' & 'upload_photo' & 'upload_audio' & 'record_video' & 'recordd_audio'
    time.sleep(2)
    m = bot.send_photo(message.chat.id, photo=first_photo, caption='متن اولیه', reply_markup=key1)
    global mid
    mid = m.message_id
    time.sleep(3)

key2 = types.InlineKeyboardMarkup()
btn2 = types.InlineKeyboardButton('دکمه جدید', callback_data='btn2')
key2.add(btn2)

@bot.callback_query_handler(func=lambda call: call.data == 'btn1')
def change(call):
    bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=mid, reply_markup=key2)

    time.sleep(3)

    bot.delete_message(chat_id=call.message.chat.id, message_id=mid)
    bot.send_message(chat_id=call.message.chat.id, text='پیام حذف شد')


bot.infinity_polling()
