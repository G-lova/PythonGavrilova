# 2. Требуется найти наименьший натуральный делитель целого числа N, отличный от 1.

# Пример:
# Для n = 15: Ответ: 3
# Для n = 35: Ответ: 5

n = int(input('Введите число: '))
count = 0
for i in range(2, n):
    if n % i == 0:
        count += 1
        print(f'Наименьший натуральный делитель числа {n} равен {i}')
        break
if count == 0:
    print("Число является простым")