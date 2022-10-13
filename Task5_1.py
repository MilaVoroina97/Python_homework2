import time
from random import randint
start_time = time.time()


check = 0
while check <= 100:
    for x in range(randint(5,25)):
            for y in range(randint(5,25)):
                for z in range(randint(5,25)):
                    
                    print(not (x or y or z) == (not x and not y and not z))
                    print(x, y, z)
    check += 1

end_time = time.time()
print("Время выполнения программы: ", (end_time-start_time) // 60, "минут")
