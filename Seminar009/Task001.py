from telegram import Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler

token_test1 = ""

bot = Bot(token=token_test1)
updater = Updater(token=token_test1)
dispatcher = updater.dispatcher

def start(update, context):
    text = update.message.text
    text_list = []
    for i in text.split():
        if 'абв' not in i:
            text_list.append(i)
    context.bot.send_message(update.effective_chat.id, ' '.join(text_list))
    
start_handler = MessageHandler(Filters.text, start)

dispatcher.add_handler(start_handler)

updater.start_polling()
updater.idle()

