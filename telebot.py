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

def weather(bot, update):
    chat_id = update.message.chat_id
    message = str(update.message.text)
    lst = message.split(" ", 1)
    location = lst[1]
    bot.send_message(chat_id=chat_id, text=getWeather(location=str(location)))

if __name__ == "__main__":
    main()