# 2) Создайте программу для игры в ""Крестики-нолики"" человек vs человек.

# 1 | 2 | X
# 4 | X | O
# X | 8 | O

def PrintGameTable(table):    # вывод таблицы на экран
    for i in range(9):
        if (i + 1) % 3 == 0:
            print(table[i])
        else:
            print(table[i], end = " | ")

def GameXO():
    table = [i for i in range(1,10)]
    PrintGameTable(table)
    xo = ("X", "O")
    step = 0
    result = "Ничья"
    while step < 9:
        for item in xo:
            player = int(input(f"Ход {item}: "))
            if player not in table:
                player = int(input("Такой ход не существует. Попробуйте еще раз: "))
            for i in table:
                if i == player:
                    table[i-1] = item
                
            PrintGameTable(table)
            if (table[0] == table[1] == table[2] or table[3] == table[4] == table[5] 
            or table[6] == table[7] == table[8] or table[0] == table[3] == table[6]
            or table[1] == table[4] == table[7] or table[2] == table[5] == table[8]
            or table[0] == table[4] == table[8] or table[2] == table[4] == table[6]):
                result = "Игрок " + item + " выиграл"
                break
            else:
                step += 1
                if step == 9:
                    break
        if (result != "Ничья"):
            break
    print(result)
    
GameXO()