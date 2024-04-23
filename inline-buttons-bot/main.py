import os
from dotenv import load_dotenv
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, \
CommandHandler, ContextTypes, CallbackContext, CallbackQueryHandler

load_dotenv()

async def say_hello(update: Update, context: ContextTypes.DEFAULT_TYPE):

    keyboard = InlineKeyboardMarkup([
        [
            InlineKeyboardButton(text="Say hello", callback_data="Hello"),
            InlineKeyboardButton(text="Say wow", callback_data="Wow"),
            InlineKeyboardButton(text="Say Bye", callback_data="Bye"),
        ],
        [InlineKeyboardButton(text="Wikipedia", url="www.wikipedia.com")],    
    ])

    await update.message.reply_text("Hello World!", reply_markup=keyboard)

async def button_controller( update: Update, context: CallbackContext ):

    data = update.callback_query.data
    if( data == "Hello" ):
        await update.callback_query.message.edit_text("Hello Hello Hello", reply_markup=None)
        return
    
    await update.callback_query.answer( text=data,show_alert=True )
    await update.callback_query.message.reply_text(data)


async def send_link(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if len(context.args) >= 2:
        button_name = context.args[0]
        link = context.args[1]
        keyboard = InlineKeyboardMarkup([[InlineKeyboardButton(button_name, url=link)]])
        await update.message.reply_text("Go to this site!!!", reply_markup=keyboard)
    else:
        await update.message.reply_text("Please provide button name and link.")
        

TOKEN = os.environ.get('TELEGRAM_BOT_TOKEN')
application = ApplicationBuilder().token(TOKEN).build()

application.add_handler( CommandHandler( "start", say_hello ) )
application.add_handler( CommandHandler("link", send_link) )
application.add_handler( CallbackQueryHandler(button_controller) )

application.run_polling(allowed_updates=Update.ALL_TYPES)