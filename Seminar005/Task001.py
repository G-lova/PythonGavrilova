# 1) Создайте программу для игры с конфетами человек против бота.
# Условие задачи: На столе лежит 120 конфета. Играют два игрока делая ход друг после друга.
# Первый ход делает человек. За один ход можно забрать не более чем 28 конфет.
# Победитель - тот, кто оставил на столе 0 конфет.

# 120 21 ---> 99 бот 4 -> 95 .... бот --->29 --> 27 >> 2конф

# a) Добавьте игру против бота

# Доп b) Подумайте как наделить бота ""интеллектом"" (Теория игр)

import random

def GameRandom(n):
    result = "Вы выиграли!"
    while n > 28:
        human = int(input("Ваш ход: "))
        if human > 28:
            human = int(input("Введите число не больше 28: "))
        n = n - human
        print(f"Осталось: {n}")
        if n < 29:
            result = "Бот выиграл!"
            break
        else:
            bot = random.randint(1, 28)
            print(f"Бот взял: {bot}")
        n = n - bot
        print(f"Осталось: {n}")
    print(result)

def GameIntellect(n):
    result = "Вы выиграли!"
    while n > 28:
        human = int(input("Ваш ход: "))
        if human > 28:
            human = int(input("Введите число не больше 28: "))
        n = n - human
        print(f"Осталось: {n}")
        if n < 29:
            result = "Бот выиграл!"
            break
        elif (n % 28) != 1:
            bot = n % 28 - 1
        else:
            bot = random.randint(1, 28)
        print(f"Бот взял: {bot}")
        n = n - bot
        print(f"Осталось: {n}")
    print(result)

# GameRandom(120)

GameIntellect(120)