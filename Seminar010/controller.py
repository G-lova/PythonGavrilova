from model import Addition_Process, Get_Addition_List
from logger import log

def result (update, context):
    log(update, context)
    text = update.message.text
    context.bot.send_message(update.effective_chat.id, f"Ваш результат: {Addition_Process(Get_Addition_List(text))}")
    