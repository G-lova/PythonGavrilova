def get_data_value():
    data_value = []
    data_value.append(input("Введите фамилию: "))
    data_value.append(input("Введите имя: "))
    data_value.append(input("Введите номер телефона: "))
    data_value.append(input("Введите комментарий: "))
    return data_value

def read_data(path):
    with open(path, 'r', encoding='utf-8') as data:
        for line in data:
            print(line)