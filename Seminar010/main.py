from telegram import Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler
from view import start
from controller import result

token_test1 = ""

bot = Bot(token=token_test1)
updater = Updater(token=token_test1)
dispatcher = updater.dispatcher

start_handler = CommandHandler('start', start)
resilt_handler = MessageHandler(Filters.text, result)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(resilt_handler)

if __name__ == '__main__':
    updater.start_polling()
    updater.idle()