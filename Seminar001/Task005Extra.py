# (!!!Доп!!!) Напишите программу для проверки истинности утверждения 
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
# (0,0,0), (0,0,1) и тд.

for x in range(2):
    for y in range(2):
        for z in range(2):
            print(f'({x},{y},{z}) {(not (x and y and z)) == ((not x) or (not y) or (not z))}')