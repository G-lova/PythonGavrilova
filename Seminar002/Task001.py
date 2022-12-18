# 1. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

# Пример:
# пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

n = int(input('Введите число: '))
count = 1
list_factorial = []
for i in range(1,n+1):
    count *= i
    list_factorial.append(count)
print(list_factorial)