from logger import logger

def get_data_teacher():
    data_value = []
    data_value.append(dialog_with_teacher("Seminar008/DataScience/Students.txt", info= "ученика"))
    data_value.append(dialog_with_teacher("Seminar008/DataScience/Subjects.txt", info= "предмет"))
    data_value.append(input("Введите оценку: "))
    return data_value

def get_data_student():
    data_value = []
    data_value.append(dialog_with_student("Seminar008/DataScience/Students.txt", info= "ученика"))
    return data_value

def read_data(data):
    with open(f"Seminar008/DataScience/{data[0]}.txt", 'r', encoding='utf-8') as student:
        for line in student:
            print(line.rstrip())

def dialog_with_teacher(path, info= None):
    print(f"\nВыберите {info}:")
    dict_elements = view_elements(path)
    print(f"{max(dict_elements) + 1} Добавить {info}")
    return choosing_result(path, dict_elements)

def dialog_with_student(path, info= None):
    print(f"\nВыберите {info}:")
    dict_elements = view_elements(path)
    return choosing_result(path, dict_elements)

def view_elements(path):
    elements = {}
    with open(path, 'r', encoding='utf-8') as file:
        i = 1
        for line in file:
            elements[i] = line.split()
            i += 1
    for key, val in elements.items():
        print(f'{key} {" ".join(val)}')
    return elements

def choosing_result(path, dict):
    element_number = int(input())
    if element_number in dict:
        return " ".join(dict[element_number])
    elif element_number == max(dict) + 1:
        return add_element(path, dict)
    else:
        print(f"\nПопробуйте еще раз:")
        choosing_result(path, dict)

def add_element(path, dict):
    dict[max(dict) + 1] = list(map(str, input("Введите новый элемент: ").split()))
    with open(path, 'w', encoding='utf-8') as file:
        for val in dict:
            file.writelines(f'{" ".join(dict[val])}\n')
    logger(" ".join(dict[max(dict)]), info= "добавлен элемент")
    return " ".join(dict[max(dict)])