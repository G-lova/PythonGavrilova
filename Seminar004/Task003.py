# 3. Задайте последовательность чисел. Напишите программу, которая выведет 
# список неповторяющихся элементов исходной последовательности.

# Ввод:
# 3 1 2 3
# Вывод:
# 2 1

n = int(input("Введите количество элементов списка: "))
min = int(input("Введите минимальный элемент списка: "))
max = int(input("Введите максимальный элемент списка: "))
from random import randint
list = [randint(min, max) for i in range(n)]
print(list)

list_final = []
for i in list:
    if list.count(i) < 2:
        list_final.append(i)

print(list_final)