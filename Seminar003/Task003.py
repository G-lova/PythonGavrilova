# 3. Задайте список из вещественных чисел. Напишите программу, 
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

n = int(input("Введите количество элементов списка: "))
min_element = float(input("Введите минимальный элемент списка: "))
max_element = float(input("Введите максимальный элемент списка: "))
import random
lst = [round(random.uniform(min_element, max_element+1),3) for i in range(n)]
print(lst)

lst_fraction = [round(lst[i]%1,3) for i in range(n)]
print(f"Разница между макс. и мин. значением дробной части элементов равна: {max(lst_fraction)} - {min(lst_fraction)} = {max(lst_fraction) - min(lst_fraction)}")