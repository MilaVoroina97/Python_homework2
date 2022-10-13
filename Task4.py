# Напишите программу, которая принимает на вход N, и координаты двух точек и находит расстояние между ними 
# в N-мерном пространстве.
from cmath import sqrt
import math

def check_digit(text):
    check = False
    while not check:
        try:
            number = float(input(f"{text}"))
            check = True
        except ValueError as error:
            print(f"Пожалуйста, введите ИМЕННО число - {error}")
    return number

def fill_coordinate(N):
    array_coordinat = []
    buff = 0
    for i in range(N):
        buff = check_digit(f'Введите координату {i+1}: ')
        array_coordinat.append(buff)
    return array_coordinat

def calculate_distance(array_coordinat1,array_coordinat2):
    result = 0
    for i in range(len(array_coordinat1)):
        result = result + pow((array_coordinat2[i] - array_coordinat1[i]),2)
    return result

try:

    n = int(input('Введите число N для определения размерности пространства: '))
    coordinat1 = fill_coordinate(n)
    coordinat2 = fill_coordinate(n)
    result = calculate_distance(coordinat1,coordinat2)
    print(f'Расстояние между двумя точками в {n}D пространстве равно: {round(math.sqrt(result),3)} ')

except:
    print("Размерность должна задаваться именно ЦЕЛЫМ ЧИСЛОМ.")

    



