"""
Задание №2
Погружение в Python | Коллекции
Пользователь вводит данные. Сделайте проверку данных
и преобразуйте если возможно в один из вариантов ниже:
✔ Целое положительное число
✔ Вещественное положительное или отрицательное число
✔ Строку в нижнем регистре, если в строке есть
хотя бы одна заглавная буква
✔ Строку в нижнем регистре в остальных случаях
"""
#
# lst = [1, 2.1, True, -5, "Sds"]
# for el in lst:
#     try:
#         print(int(el))
#         print(float(el))
#     except ValueError:
#         print(f"Невозможно преобразовать {el} к целому положительному числу")
#         print(f"Невозможно преобразовать {el} к вещественному числу")
#
# for el in lst:
#     try:
#         if type(el) == str and not el.islower():
#             print(el.lower())
#     except TypeError:
#         print("Ошибка")
#

# вариант 2

a = input("Введите данные: ")

if a.isdigit():
    a = int(a)
elif a.replace(".", "").replace("-", "").isdigit()\
    and a.count(".") == 1\
    and a.count("-") <= 1\
    and (a.count("-") == 1 and a.startswith("-")):
    a = float(a)
elif a != a.lower():
    a = a.lower()
else:
    a = a.upper()

print(type(a), a)
