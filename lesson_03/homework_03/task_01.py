# Задача 1.
# Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами.
# В результирующем списке не должно быть дубликатов.

lst = [1, 2, 5, 8, 2, 11, 3, 8, 1, 24, 7, 16, 10, 11]

count_dict = {}
for item in lst:
    count_dict[item] = count_dict.get(item, 0) + 1
repeat_elems = [key for key in count_dict.keys() if count_dict[key] > 1]
print(repeat_elems)


# Другой вариант выполнения задания

def find_duplicates(lst):
    return list(set([x for x in lst if lst.count(x) > 1]))


lst = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
print(find_duplicates(lst))
