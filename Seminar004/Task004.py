# 4. Задана натуральная степень k. Сформировать случайным образом список коэффициентов 
# (значения от 0 до 100) многочлена и вывести многочлен степени k.

# Пример:
# k = 2 => 2*x² + 4*x + 5 
# k = 6 => ix^6 + ax^5 + bx^4+ cx^3 + dx^2 + ex + h

# a, b, c, d, e, h - рандом

k = int(input("Введите k: "))
from random import randint
list_coeff = [randint(0, 100) for i in range(k+1)]


equation = ""
for i in list_coeff:
    if i != 0:
        if k > 1:
            equation += str(i) + "x^" + str(k) + " + "
            k -= 1
        elif k == 1:
            equation += str(i) + "x" + " + "
            k -= 1
        else:
            equation += str(i)
    else:
        k -= 1
print(equation)
