# 3) Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# Пример:
# - 6782 -> 23
# - 0,56 -> 11

num = input("Введите число: ")
lst = list(map(int, [i for i in num if i.isdigit()]))
sum = lst[0]
for i in range(1, len(lst)):
    sum += lst[i]
print(sum)