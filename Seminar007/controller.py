from model import init, add_data
from view import read_data, get_data_value
from logger import logger

path1 = "Seminar007/PhoneBookTable.txt"
path2 = "Seminar007/PhoneBookString.txt"

def dialog():
    print("Выберите номер операции:")
    print("1 - Добавление данных")
    print("2 - Просмотр данных\n")
    enter = input()
    if enter == "1":
        name_data = get_data_value()
        init(name_data)
        add_data(name_data, path1, path2)
        logger(", ".join(name_data), info='добавлены данные')
    elif enter == "2":
        read_data(path2)
        logger(None, info='просмотрены данные')
    else:
        dialog()