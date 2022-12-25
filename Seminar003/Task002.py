# 2. Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

n = int(input("Введите количество элементов списка: "))
min = int(input("Введите минимальный элемент списка: "))
max = int(input("Введите максимальный элемент списка: "))
from random import randint
list = [randint(min, max+1) for i in range(n)]
print(list)

list_product = []
for i in range(int(n/2+0.5)):
    list_product.append(list[i]*list[n-1-i])
print(list_product)