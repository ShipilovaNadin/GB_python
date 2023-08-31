"""
Задание №3
✔ Функция получает на вход строку из двух чисел через пробел.
✔ Сформируйте словарь, где ключом будет
символ из Unicode, а значением — целое число.
✔ Диапазон пар ключ-значение от наименьшего из введённых
пользователем чисел до наибольшего включительно
"""


def func(data):
    dct = {chr(int(el)): el for el in sorted(data.split())}
    return dct


print(func('1 4 3'))


def uni_symb(text: str) -> dict[str, int]:
    lst = list(map(int, text.split()))
    symb = {}
    for i in range(min(lst), max(lst)):
        symb[chr(i)] = i
    return symb


numms = input("Введите цифры: ")
dict_ = uni_symb(numms)
print(dict_)
