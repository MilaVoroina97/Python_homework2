# Напишите программу, которая принимает на вход N, и координаты двух точек и находит расстояние между ними 
# в N-мерном пространстве.
import math
n = int(input('Введите число N для определения размерности пространства: '))
coordinat1 = []
buff1 = 0
for i in range(n):
    buff = float(input('Введите координаты первой точки: '))
    coordinat1.append(buff1)
coordinat12 = []
buff2 = 0
for j in range(n):
    buff2 = float(input('Введите координаты второй точки: '))
    coordinat12.append(buff2)
result = []
buff = 0
for k in range(n):
    buff = buff + pow((coordinat12[k] - coordinat1[k]),2)
    result.append(buff)
    print(result)
print()
print(math.sqrt(result))

    



