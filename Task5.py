# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z . Но теперь количество предикатов не три,
#  а генерируется случайным образом от 5 до 25, проверяем это утверждение 100 раз, с помощью модуля time выводим на экран , 
#  сколько времени отработала программа.

import time
start_time = time.time()

check = 0
while check <= 100:
    for x in range(5,25):
            for y in range(5,25):
                for z in range(5,25):
                    
                    print(not (x or y or z) == (not x and not y and not z))
                    print(x, y, z)
    check += 1

end_time = time.time()
print("Время выполнения программы: ", (end_time-start_time) // 60, "минут")
                    





