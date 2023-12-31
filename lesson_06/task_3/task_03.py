"""
Улучшаем задачу 2.
Добавьте возможность запуска функции “угадайки” из модуля в командной строке терминала.
Строка должна принимать от 1 до 3 аргументов: параметры вызова функции.
Для преобразования строковых аргументов командной строки в числовые параметры используйте генераторное выражение.
"""

from random import randint
from sys import argv

def bigger_or_equal(argv):
    num = randint(args[0], args[1])
    i = 0
    while argv[2] > i:
        u_num = int(input(f"Введите число от {args[0]} до {args[1]}: "))
        if u_num > num:
            print("Меньше!")
        elif u_num < num:
            print("Больше!")
        else:
            print("Угадал!")
            return True
        i += 1
    return False


args = [int(el) for el in argv[1:]]
print(bigger_or_equal(args))