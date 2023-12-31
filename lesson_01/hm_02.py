"""
Напишите код, который запрашивает число и сообщает является ли оно простым или составным. Используйте правило для
проверки: “Число является простым, если делится нацело только на единицу и на себя”.
Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.
"""
num = int(input("Введите число от 0 до 100 000: "))
MIN_NUM = 0
MAX_NUM = 100000
if num < MIN_NUM or num > MAX_NUM:
    print("Вы ввели число вне заданного диапазона")
else:
    k = 0
    for i in range(2, num // 2+1):
        if (num % i == 0):
            k += 1
    if k<= 0:
        print("Число простое")
    else:
        print("Число не является простым")