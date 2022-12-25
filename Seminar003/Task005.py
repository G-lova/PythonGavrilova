# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

def fib(n):
    if n in [1,2]:
        return 1
    elif n > 1:
        return fib(n-1) + fib(n-2)
    else:
        return fib(n+2) - fib(n+1)

m = int(input("Введите число: "))
lst_fib = []
for i in range(-m,m+1):
    lst_fib.append(fib(i))
print(lst_fib)