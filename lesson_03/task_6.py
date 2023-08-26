"""
Задание №6
Погружение в Python | Коллекции
Пользователь вводит строку текста. Вывести каждое слово с новой строки.
✔ Строки нумеруются начиная с единицы.
✔ Слова выводятся отсортированными согласно кодировки Unicode.
✔ Текст выравнивается по правому краю так, чтобы у самого длинного
слова был один пробел между ним и номером строки.
"""

texts = "vsdsdsdsdsds dfsfdf fdfdfd fdfdfd".split()
shift = len(max(texts))
for n, el in enumerate(sorted(texts), 1):
    print(f"{n}, {el:>{shift}}")



words = input('Введите строку: ').split()
max_len = len(max(words, key=len))
sorted_words = sorted(words, key=lambda word: word.lower())
for i, word in enumerate(sorted_words, 1):
    print(f'{i} {word.rjust(max_len + 1)}')