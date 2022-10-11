# Задача 1. Напишите программу, которая принимает на вход вещественное или целое число и показывает сумму его цифр.
#  Через строку нельзя решать.

# *Пример:*

# - 6782 -> 23
# - 0,56 -> 11

def number_sum(n):
    symbols = ('.')
    sum = 0
    if symbols in n:

        buff = n.split('.')
        buff1 = int(buff[0])
        buff2 = int(buff[1])
        while buff1 != 0:
            sum = sum + buff1 % 10
            buff1 = buff1 // 10
        while buff2 != 0:
            sum = sum + buff2 % 10
            buff2 = buff2 // 10
    else:
        n1 = int(n)
        while n1 != 0:
            sum = sum + n1 % 10
            n1 = n1 //10
    return sum


try:
    number = input('Please enter a number:')
    print(f'Сумма цифр в числе {number} = {number_sum(number)}')
except:
    print('Please enter a positive float number with dot {.} or integer number. ')



    






