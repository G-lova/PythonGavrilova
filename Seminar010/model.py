def Get_Addition_List(text: str):
    new_text = ""
    for i in text:
        if i != " ":
            new_text += i
    if "-" in new_text:
        new_text = new_text.replace("-", "+-")
    if "," in new_text:
        new_text = new_text.replace(",", ".")   
    data_addition = new_text.split("+")
    return data_addition

def Addition_Process(data_addition):
    data_addition_list = []
    for i in data_addition:
        temp_list = Get_List(i)
        if "*" or "/" in temp_list:
            data_addition_list.append(Prod_Div(temp_list))
        else:
            data_addition_list.append(float(temp_list))
    return sum(data_addition_list)
    
def Get_List(text: str):
    data_list = []
    num = text[0]
    for i in range(1, len(text)):
        if text[i] == "*" or text[i] == "/":
            data_list.append(float(num))
            data_list.append(text[i])
            num = ""
        else:
            num += text[i]
    data_list.append(float(num))
    return data_list

def Prod_Div(data: list):
    data_list = data.copy()
    for count in range(data_list.count("*") + data_list.count("/")):
        for i in range(len(data_list)):
            if data_list[i] == "*":
                temp = data_list[i-1] * data_list[i+1]
                data_list[i] = temp
                data_list.pop(i+1)
                data_list.pop(i-1)                
                break
            elif data_list[i] == "/":
                temp = data_list[i-1] / data_list[i+1]
                data_list[i] = temp
                data_list.pop(i+1)
                data_list.pop(i-1)
                break
    return data_list[0]
  
                

# expression = input("Введите выражение: ")
# print(Get_Addition_List("2*3+4*5/2-6/2*5+1"))
# print(Addition_Process(Get_Addition_List("2*3+4*5/2-6/2*5+1")))



