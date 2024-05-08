import os
from dotenv import load_dotenv
from telebot import TeleBot
from telebot.types import Message

load_dotenv()

TOKEN = os.environ.get("TOKEN")
bot = TeleBot(token=TOKEN)


# Download photo from telegram channels
def file_name(m: str):
    return m.split('/')[-1]

@bot.message_handler(content_types=['photo'])
def download_photo(message: Message):
    file_id = message.photo[-1].file_id
    file_path = bot.get_file(file_id)
    print(file_path.file_path)
    d_path = bot.download_file(file_path.file_path)
    with open(f"{file_name(file_path.file_path)}", 'wb') as newfile:
        newfile.write(d_path)





if __name__ == '__main__':
    bot.polling()
