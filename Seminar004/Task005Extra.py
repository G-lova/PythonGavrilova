# 5. Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.

# 2*x^2 + 4*x      5*x^2 + 2*x
#     7x^2 + 6x

# 2*x^6 + 4*x      5*x^2 + 2*x
#     2*x^6 + 5x^2 + 6x

def Get_Data(path): # получаю данные
    with open(path, 'r') as data:
        for line in data:
            return line

def Get_List_Equation(path): # представляю полученные многочлены в виде списка отдельных членов
    line = Get_Data(path)
    new_line = ""
    for i in line:
        if i != " ":
            new_line += i
    if "-" in new_line:
        new_line = new_line.replace("-", "+-")      
    return new_line.split("+")
     
def Get_Max_Stepen(path): # определяю максимально возможную степень нового многочлена
    line = Get_Data(path)
    new_line = ""
    for i in line:
        if i.isdigit():
            new_line += i
        else:
            new_line += " "
    stepen = new_line.split(" ")
    final_stepen = [1]
    for i in stepen:
        if i != "":
            final_stepen.append(i)
    return max(map(int,final_stepen))

def Get_Coeff(path): # создаю список из соответствующих коэффициентов многочленов
    list_coeff = []
    for i in range(Get_Max_Stepen(path) + 1):
        list_coeff.append(0)
    
    for i in Get_List_Equation(path):
        list = i.split("*")
        if len(list) == 1:
            if list[0] == "x":
                list_coeff[1] = 1
            elif "x^" in list[0]:
                list_coeff[int(list[0].replace("x^", ""))] = 1
            else:
                list_coeff[0] = int(list[0])
        else:
            if list[1] == "x":
                list_coeff[1] = int(list[0])
            else:
                list_coeff[int(list[1].replace("x^", ""))] = int(list[0])
    return list_coeff

def Get_Polinomial(list_coeff): # создаю список из коэффициентов для нового многочлена
    polinomial = []
    for i in list_coeff:
        if list_coeff.index(i) == 0:
            if i != 0:
                polinomial.append(i)
        elif list_coeff.index(i) == 1:
            if i != 0:
                if i == 1:
                    polinomial.insert(0, "x")
                else:
                    polinomial.insert(0, str(i) + "*x")
        else: 
            if i != 0:
                if i == 1:
                    polinomial.insert(0, "x^" + str(list_coeff.index(i)))
                else:
                    polinomial.insert(0, str(i) + "*x^" + str(list_coeff.index(i)))
    return " + ".join(map(str,polinomial))

path1 = 'Seminar004/Equation1.txt'
path2 = 'Seminar004/Equation2.txt'
path3 = 'Seminar004/Equation3.txt'

print(Get_Data(path1))
print(Get_Data(path2))

list_coeff1 = Get_Coeff(path1)
list_coeff2 = Get_Coeff(path2)

# получаю новый многочлен-сумму и добавляю в новый файл:

while len(list_coeff1) != len(list_coeff2):
    if len(list_coeff1) > len(list_coeff2):
        list_coeff2.append(0)
    else:
        list_coeff1.append(0)

list_coeff = []
for i in range(len(list_coeff1)):
    list_coeff.append(list_coeff1[i] + list_coeff2[i])
    
with open(path3, 'w') as data:
    data.write(Get_Polinomial(list_coeff))

print(Get_Polinomial(list_coeff))