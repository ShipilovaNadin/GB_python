"""
Задание №5
✔ Доработаем предыдущую задачу.
✔ Создайте новую функцию которая генерирует файлы с разными расширениями.
✔ Расширения и количество файлов функция принимает в качестве параметров.
✔ Количество переданных расширений может быть любым.
✔ Количество файлов для каждого расширения различно.
✔ Внутри используйте вызов функции из прошлой задачи.
"""

from Lessson_07.task_4.task_4 import func

def func_task_5(extensions, counts):
    for extension, count in zip(extensions, counts):
        func(extension, min_len=1, max_len=3, min_rand_bytes=25, max_rand_bytes=409, files=count)


extens = ['.cvc', '.pdf', '.doc']
counts_files = [1, 2, 2]

func_task_5(extens, counts_files)