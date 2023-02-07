from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import datetime

def log(update, context):
    file = open('Seminar009/Task002Extra/log.csv', 'a', encoding='utf-8')
    file.write(f'{datetime.datetime.now().time()}, {update.effective_user.first_name}, {update.effective_user.id}, {update.message.text}\n')
    file.close() 