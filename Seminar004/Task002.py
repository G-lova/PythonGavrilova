# 2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# N = 6 | N = 12    | 32                | 13 | 9     | 18        | 21
# 2 * 3 | 2 * 2 * 3 | 2 * 2 * 2 * 2 * 2 | 13 | 3 * 3 | 2 * 3 * 3 | 3*7

n = int(input("Введите число: "))
lst = []
count = 0
while n > 1:
    for i in range(2, n+1):
        if n % i == 0:
            lst.append(i)
            n = int(n/i)
            count += 1
            break
print(' * '.join(map(str, lst)))