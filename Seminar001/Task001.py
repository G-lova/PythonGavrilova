# 1. Напишите программу, которая принимает на вход цифру, обозначающую день недели,
# и проверяет, является ли этот день выходным.

# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет

print('Введите день недели цифрой: ')
week_figure = int(input())
if 5 < week_figure < 8:
    print('True')
elif week_figure < 1 or week_figure > 7:
    print('Вы некорректно ввели день недели')
else:
    print('False')