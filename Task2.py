# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

# *Пример:*

# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

def multiplication(n):
    count = 1
    for i in range(1, n + 1):
        count *= i
    return count

def check_digit(text):
    check = False
    while not check:
        try:
            number = int(input(f"{text}"))
            check = True
        except ValueError:
            print("Пожалуйста, введите именно ЦЕЛОЕ число.")
    return number

number = check_digit('Пожалуйста, введите любое положительное целое число: ')
result = []
for i in range(1, number + 1):
    result.append(multiplication(i))
print(f'Произведение чисел от 1 до {number} = {result}')
