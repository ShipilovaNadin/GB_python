"""
Задание №4
✔ Напишите программу, которая вычисляет площадь
круга и длину окружности по введённому диаметру.
✔ Диаметр не превышает 1000 у.е.
✔ Точность вычислений должна составлять
не менее 42 знаков после запятой.
"""
import decimal
import math

r = int(input('Введите радиус: '))

i = 2 * r * 3.14  # Длина окружности

s = 3.14 * r ** 2  # Площадь круга

print(f"Длина окружности: {i:.42f}, площадь круга: {s:.42f}")

""" Вариант 2"""
LEN_DIG = 42
MAX_D = 1000
PI = decimal.Decimal(math.pi)

decimal.getcontext().prec = LEN_DIG
diameter = decimal.Decimal(input("Введите диаметр окружности: "))
if diameter > MAX_D:
    print("Превысили допустимое значение диаметра")
else:
    len_circles = PI * diameter
    area_circles = PI * diameter ** 2 / 4
    print(f"{len_circles=}\n{area_circles=}")
