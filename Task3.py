# Напишите программу, в которой пользователь будет задавать две строки, а программа - определять количество вхождений
# одной строки в другой.

from re import sub


def count_substring(string1,string2):
    len1 = len(string1)
    len2 = len(string2)
    count = 0
    i = 0
    if len1 > len2:
        while i < len1:
            if string1[i:i+ len2] == string2:
                count += 1
            i += 1
        print(f'Количество вхождений второй строки в первую: {count}')
    else:
        print('Пожалуйста, обратите внимание, что первая строка должна быть длиннее, чем вторая.')

string = input('Пожалуйста, введите первую строку')
substring = input('Пожалуйста, введите подстроку: ')
count_substring(string,substring)



  
            









