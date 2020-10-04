from telegram.ext import Updater, CommandHandler, InlineQueryHandler, MessageHandler
import telegram.message
from weather import getWeather

def main():
    MY_TOKEN_ID = "TOKEN"
    updater = Updater(MY_TOKEN_ID)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("clima", weather))
    updater.start_polling()
    updater.idle()

