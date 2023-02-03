import os.path

data = []

def init(name_list):
    global data
    data = name_list


def add_data(data):
    path = "Seminar008/DataScience/" + data[0] + ".txt"
    if os.path.isfile(path):
        if find_text(data[1], path) == True:
            mark_list = []
            with open(path, 'r', encoding='utf-8') as student:
                for line in student:
                    if data[1] in line.split():
                        mark_list.append(f"{line.rstrip()} {data[2]}\n")
                    else:
                        mark_list.append(line)
            with open(path, 'w', encoding='utf-8') as student:
                student.writelines(mark_list)
        else:
            with open(path, 'a', encoding='utf-8') as student:
                student.write(f"{data[1]} {data[2]}\n")
    else:
        with open(path, 'w', encoding='utf-8') as student:
            student.write(f"{data[1]} {data[2]}\n")
    print("Данные успешно сохранены")

def find_text(text, f_path):
    with open(f_path, 'r', encoding='utf-8') as f:
        in_file = False
        for line in f:
            if text in line:
                in_file = True
                break
    return in_file