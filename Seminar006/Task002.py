# 2) Дан список, вывести отдельно буквы и цифры, пользуясь filter.

# [12,'sadf',5643] ---> ['sadf'] ,[12,5643]

# Все задачи решать с помощью использования лямбд, filter, map, zip, enumerate, List Comprehension

lst = [12, 'sadf', 5643, 'duf', 46]
lst_num = list(filter(lambda x: type(x) == int, lst))
lst_text = list(filter(lambda x: type(x) == str, lst))
print(lst_num, lst_text)
