"""
Напишите однострочный генератор словаря, который принимает на вход три списка одинаковой длины: имена str, ставка int,
премия str с указанием процентов вида “10.25%”. В результате получаем словарь с именем в качестве ключа и суммой премии
в качестве значения. Сумма рассчитывается как ставка умноженная на процент премии
"""


names_list = ["Petrov", "Ivanov", "Sidorov"]
rates_list = [10000, 15000, 20000]
percent_list = ["10.25%", "15.25%", "5.25%"]

my_dict = {name: rate * float(percent.rstrip("%")) / 100
           for name, rate, percent in zip(names_list, rates_list, percent_list)}

print(my_dict)


def generate_salary_dict(names_list, salaries_list, bonuses_list):
    return {name: salary * (1 + float(bonus.strip('%')) / 100) for name, salary, bonus in zip(names_list, salaries_list, bonuses_list)}

names = ["Alice", "Bob", "Charlie"]
salaries = [10000, 15000, 20000]
bonuses = ["10%", "15%", "20%"]

salary_dict = generate_salary_dict(names, salaries, bonuses)
print(salary_dict)

