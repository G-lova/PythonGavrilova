from telegram import Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler
from model import *

token_test1 = ""

bot = Bot(token=token_test1)
updater = Updater(token=token_test1)
dispatcher = updater.dispatcher

start_handler = CommandHandler('start', start)
rules_handler = CommandHandler('rules', rules)
end_handler = CommandHandler('end', end)
play_handler = CommandHandler('play', play)
turn_cycle_handler = MessageHandler(Filters.text, turn_cycle)
human_turn_handler = MessageHandler(Filters.text, human_turn)
cancel_handler = CommandHandler('cancel', cancel)
conv_handler = ConversationHandler(entry_points=[play_handler],
                                    states={A: [turn_cycle_handler]},
                                    fallbacks=[cancel_handler])

dispatcher.add_handler(start_handler)
dispatcher.add_handler(rules_handler)
dispatcher.add_handler(end_handler)
dispatcher.add_handler(play_handler)
dispatcher.add_handler(turn_cycle_handler)
dispatcher.add_handler(human_turn_handler)
dispatcher.add_handler(conv_handler)

if __name__ == '__main__':
    updater.start_polling()
    updater.idle()