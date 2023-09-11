"""
Напишите функцию группового переименования файлов. Она должна:
принимать параметр желаемое конечное имя файлов. При переименовании в конце имени добавляется порядковый номер.
принимать параметр количество цифр в порядковом номере.
принимать параметр расширение исходного файла. Переименование должно работать только для этих файлов внутри каталога.
принимать параметр расширение конечного файла.
принимать диапазон сохраняемого оригинального имени. Например для диапазона [3, 6] берутся буквы с 3 по 6 из исходного
имени файла. К ним прибавляется желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение.
"""

import os

def batch_rename(new_name, digits, source_ext, dest_ext, range_name, path='.'):
    counter = 1
    for filename in os.listdir(path):
        if filename.endswith(source_ext):
            old_name = os.path.splitext(filename)[0] # get the name without extension
            old_name_substring = old_name[range_name[0]:range_name[1]] if range_name else ""
            new_filename = f"{old_name_substring}{new_name}{str(counter).zfill(digits)}{dest_ext}"
            os.rename(os.path.join(path, filename), os.path.join(path, new_filename))
            counter += 1

batch_rename('new_file', 3, '.jpg', '.md', [1, 3], '/Lesson_07\\homework_07')


# def rename_file(new_name, num_of_digits, old_extension, new_extension, name_range, directory):
#     count = 1
#     for filename in os.listdir(directory):
#         if filename.endswith(old_extension):
#             old_name = filename.split('.')[0][name_range[0] - 1:name_range[1]] if name_range else ""
#             new_file_name = f'{old_name}{new_name}{str(count).zfill(num_of_digits)}.{new_extension}'
#             os.rename(os.path.join(directory, filename), os.path.join(directory, new_file_name))
#             count += 1
#
#
# rename_file('file1', 2, 'txt', 'jpg', [0, 3], 'C:\\Users\\nadin\\GB_python\\GB_python\\Lessson_07\\homework_07')