from model import init, add_data
import view
from logger import logger

def dialog():
    print("1 - Учитель")
    print("2 - Ученик\n")
    answer = input()
    if answer == "1":
        mark_data = view.get_data_teacher()
        init(mark_data)
        add_data(mark_data)
        logger(", ".join(mark_data), info='добавлены данные')
    elif answer == "2":
        student = view.get_data_student()
        view.read_data(student)
        logger(*student, info='просмотрены данные')
    else:
        dialog()