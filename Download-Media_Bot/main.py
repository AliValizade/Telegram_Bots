import os
from dotenv import load_dotenv
from telebot import TeleBot
from telebot.types import Message

load_dotenv()

TOKEN = os.environ.get("TOKEN")
bot = TeleBot(token=TOKEN)



def file_name(m: str):
    return m.split('/')[-1]

# Download photo from telegram channels
@bot.message_handler(content_types=['photo'])
def download_photo(message: Message):
    file_id = message.photo[-1].file_id
    file_path = bot.get_file(file_id)
    print(file_path.file_path)
    d_path = bot.download_file(file_path.file_path)
    with open(f"{file_name(file_path.file_path)}", 'wb') as newfile:
        newfile.write(d_path)

# Download other media from telegram channels
@bot.message_handler(content_types=['animation', 'audio', 'document', 'photo', 'sticker', 'video', 'video_note', 'voice'])
def download_media(message: Message):
    if message.content_type == 'audio':
        file_id = message.audio.file_id
        file_path = bot.get_file(file_id)
        d_path = bot.download_file(file_path.file_path)
        with open(f"{file_name(file_path.file_path)}", 'wb') as newfile:
            newfile.write(d_path)
    elif message.content_type == 'video':
        file_id = message.video.file_id
        file_path = bot.get_file(file_id)
        d_path = bot.download_file(file_path.file_path)
        with open(f"{file_name(file_path.file_path)}", 'wb') as newfile:
            newfile.write(d_path)
    elif message.content_type == 'voice':
        file_id = message.voice.file_id
        file_path = bot.get_file(file_id)
        d_path = bot.download_file(file_path.file_path)
        with open(f"{file_name(file_path.file_path)}", 'wb') as newfile:
            newfile.write(d_path)
    elif message.content_type == 'video_note':
        file_id = message.video_note.file_id
        file_path = bot.get_file(file_id)
        d_path = bot.download_file(file_path.file_path)
        with open(f"{file_name(file_path.file_path)}", 'wb') as newfile:
            newfile.write(d_path)
    elif message.content_type == 'document':
        file_id = message.document.file_id
        file_path = bot.get_file(file_id)
        d_path = bot.download_file(file_path.file_path)
        with open(f"{file_name(file_path.file_path)}", 'wb') as newfile:
            newfile.write(d_path)
    elif message.content_type == 'animation':
        file_id = message.animation.file_id
        file_path = bot.get_file(file_id)
        d_path = bot.download_file(file_path.file_path)
        with open(f"{file_name(file_path.file_path)}", 'wb') as newfile:
            newfile.write(d_path)
    elif message.content_type == 'sticker':
        file_id = message.sticker.file_id
        file_path = bot.get_file(file_id)
        d_path = bot.download_file(file_path.file_path)
        with open(f"{file_name(file_path.file_path)}", 'wb') as newfile:
            newfile.write(d_path)

    
# Get Admins-list of telegram groups or channels
@bot.message_handler(commands=['admins'])
def admins(message: Message):
    received_list = bot.get_chat_administrators(message.chat.id)
    admins_list = [item.user.first_name for item in received_list]
    print(admins_list)
    print('============')

@bot.message_handler(commands=['bloggertype'])
def admins(message: Message):
    blogger_type = bot.get_chat_member(message.chat.id, message.from_user.id)
    print(blogger_type.status)





if __name__ == '__main__':
    bot.polling()
