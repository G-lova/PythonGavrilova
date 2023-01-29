data = []

def init(name_list):
    global data
    data = name_list

def add_data(data, path1, path2):
    with open(path1, 'a', encoding='utf-8') as data_table:
        for i in data:
            data_table.write(i +'\n')
        data_table.write(10 * "-" + '\n')
    with open(path2, 'a', encoding='utf-8') as data_string:
        data_string.writelines(", ".join(data) + '\n')
    print("Данные успешно сохранены")

