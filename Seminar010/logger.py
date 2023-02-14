from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import datetime
from model import Addition_Process, Get_Addition_List

def log(update, context):
    file = open('Seminar010/log.csv', 'a', encoding='utf-8')
    file.write(f'{datetime.datetime.now().time()}, {update.effective_user.first_name}, id={update.effective_user.id}, {update.message.text}, результат={Addition_Process(Get_Addition_List(update.message.text))}\n')
    file.close() 