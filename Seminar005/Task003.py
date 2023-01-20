# 3) Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

# Входные данные хранятся в отдельных текстовых файлах.
# stroka = "aaabbbbccbbb"
# ....
# stroka = "3a4b2c3b"

# Вывод: stroka = "aaabbbbccbbb"

def Get_Data(path):
    with open(path, 'r') as data:
        for line in data:
            return line

def RLE_Symbols_to_Numbers(path):
    list = [i for i in Get_Data(path)]

    list_symbol = [list[0]]
    list_number = []
    num = 1
    for i in range(1, len(list)):
        if list[i] == list[i-1]:
            num += 1
        else:
            list_number.append(num)
            list_symbol.append(list[i])
            num = 1
    list_number.append(num)

    string_rle = ""
    for i in range(len(list_number)):
        string_rle += str(list_number[i]) + list_symbol[i]

    return string_rle

def RLE_Numbers_to_Symbols(path):
    text = Get_Data(path)
    string_rle = ""
    if text[0].isdigit():
        num = text[0]
    else:
        string_rle += text[0]
        num = ""
    for i in range(1, len(text)):
        if text[i].isdigit():
            num += text[i]
        elif num == "":
            string_rle += text[i]
            num = ""
        else:
            string_rle += int(num) * text[i]
            num = ""            
    return string_rle

path1 = 'Seminar005/File001.txt'
path2 = 'Seminar005/File002.txt'

print(f"{Get_Data(path1)} = {RLE_Symbols_to_Numbers(path1)}")
print(f"{Get_Data(path2)} = {RLE_Numbers_to_Symbols(path2)}")