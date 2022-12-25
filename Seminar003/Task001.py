# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, 
# стоящих на нечётной позиции.

# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

n = int(input("Введите количество элементов списка: "))
min = int(input("Введите минимальный элемент списка: "))
max = int(input("Введите максимальный элемент списка: "))
from random import randint
list = [randint(min, max+1) for i in range(n)]
print(list)

sum = 0
for i in range(1, n, 2):
    sum += list[i]
print(f"Сумма элементов на нечетных позициях равна: {sum}")