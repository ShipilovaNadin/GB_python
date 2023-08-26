"""
Задание №4
Погружение в Python | Коллекции
✔ Создайте вручную список с повторяющимися элементами.
✔ Удалите из него все элементы, которые встречаются дважды.
"""

lst = [1, 1, 2, 2, 3, 3, 3, 4, 5, 5]
for el_1 in lst:
    count = 0
    for el_2 in lst:
        if el_1 == el_2:
            count += 1
    lst.remove(el_1)
    lst.remove(el_1)

print(lst)

lst = [1, 2, 3, 4, 5, 1, 2, 6, 8, 10]
count_dict = {}
for item in lst:
    count_dict[item] = count_dict.get(item, 0) + 1
lst = [item for item in lst if count_dict[item] != 2]
print(lst)
