# 4. Задана натуральная степень k. Сформировать случайным образом список коэффициентов 
# (значения от 0 до 100) многочлена и вывести многочлен степени k.

# Пример:
# k = 2 => 2*x² + 4*x + 5 
# k = 6 => ix^6 + ax^5 + bx^4+ cx^3 + dx^2 + ex + h

# a, b, c, d, e, h - рандом


def Get_Polinomial(k, list_coeff):
    polinomial = ""
    for i in list_coeff:
        if i != 0:
            if k > 1:
                polinomial += str(i) + "x^" + str(k) + " + "
                k -= 1
            elif k == 1:
                polinomial += str(i) + "x" + " + "
                k -= 1
            else:
                polinomial += str(i)
        else:
            k -= 1
    return polinomial


k = int(input("Введите k: "))
from random import randint
list_coeff = [randint(0, 100) for i in range(k+1)]

print(Get_Polinomial(k, list_coeff))
