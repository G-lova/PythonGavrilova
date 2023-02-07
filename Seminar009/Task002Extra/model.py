from telegram import Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler
from random import randint
from logger import log

def start(update, context):
    log(update, context)
    context.bot.send_message(update.effective_chat.id, "Сыграем?")
    context.bot.send_message(update.effective_chat.id, 
            "/play - Конечно!\n/end - В другой раз\n/rules - Правила игры")
    
def rules(update, context):
    log(update, context)
    context.bot.send_message(update.effective_chat.id, 
            "На столе лежит 120 конфета. Игроки ходят по очереди. За один ход можно забрать не более 28 конфет. Победитель - тот, кто заберет последние конфеты.")
    context.bot.send_message(update.effective_chat.id, "Ну что, надумал?")
    context.bot.send_message(update.effective_chat.id, "/play - Да, /end - Нет")
    
def end(update, context):
    log(update, context)
    context.bot.send_message(update.effective_chat.id, "Очень жаль! Пока!")

A = 0

def play(update, context):
    log(update, context)
    context.bot.send_message(update.effective_chat.id, "На столе 120 конфет\nВаш ход")
    return A
 

def turn_cycle(update, context):
    log(update, context)
    n = 120
    result = "Вы выиграли!"
    while n > 28:
        # human = int(update.message.text)
        human = human_turn(update, context)
        # if 0 < human < 29:
        n = n - human
        context.bot.send_message(update.effective_chat.id, f"Осталось {n} конфет")
        if n < 29:
            result = "Я выиграл!"
            break
        elif (n % 28) != 1:
            bot = n % 28 - 1
        else:
            bot = randint(1, 28)
        context.bot.send_message(update.effective_chat.id, f"Я взял {bot} конфет")
        n = n - bot
        context.bot.send_message(update.effective_chat.id, f"Осталось {n} конфет")
        context.bot.send_message(update.effective_chat.id, "Ваш ход")
        # else:
        #     context.bot.send_message(update.effective_chat.id, "Вы можете взять от 1 до 28 конфет за ход")
        #     human = int(update.message.text)
    context.bot.send_message(update.effective_chat.id, result)
    context.bot.send_message(update.effective_chat.id, "Еще разок?")
    start(update, context)
    return ConversationHandler.END

   
def human_turn(update, context):
    human = int(update.message.text)
    if 0 < human < 29:
        return human
    else:
        context.bot.send_message(update.effective_chat.id, "Вы можете взять от 1 до 28 конфет за ход")
        human_turn(update, context)

def cancel(update, context):
    context.bot.send_message(update.effective_chat.id, 'Что-то пошло не так!')

