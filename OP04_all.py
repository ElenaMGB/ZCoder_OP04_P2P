# OP04
# 1. Напишите функцию sum_range(start, end), которая суммирует все целые числа от значения start до величины end включительно.

# import random

# start=float(input("Введите начало диапазона: "))
# end=float(input("Введите конец диапазона: "))
# d = random.uniform(start, end+1)
# print(my_list)
# /////////////////////


def sum_range(start, end):
    """
  Функция суммирует все целые числа от start до end включительно.

  :param start: Начальное значение диапазона (включительно)
  :param end: Конечное значение диапазона (включительно)
  :return: Сумма всех целых чисел от start до end включительно
  """
    # Используем формулу суммы арифметической прогрессии
    if start > end:
        return 0

    return sum(range(start, end + 1))


# Пример использования функции
print(sum_range(1, 10))  # Вывод: 55
print(sum_range(5, 15))  # Вывод: 110
print(sum_range(-5, 5))  # Вывод: 0

# while i<=end
# list.append(d)

# def sum_range(start, end):
#     if start > end:
#         start, end = end, start
#     return sum(range(start, end+1))

# Задаем список
# my_list=[-1, 1.5, 0, 2, 3.5, 4.5, 4, 5.5, 6.5, 7.5, 8.5, 9]
# new_list=list(filter(lambda x: x%1==0, my_list)) #
# print(new_list)

# #суммируем значения отфильтрованного списка
# sum=0
# for i in new_list:
#     sum=sum+i
# print (sum)

# def sum_range(start, end):
#   sum = 0
#   while i.type() is int:
#     for i in range(start, end + 1):
#       if i%2 == 0:
#         sum += i
#     return sum

# sum_range(1,12)

# 2.Написать функцию square, принимающую 1 аргумент — сторону квадрата, и возвращающую 3 значения (с помощью кортежа, после return перечислить все значения через запятую): периметр квадрата, площадь квадрата и диагональ квадрата.

# def square(a):
#   p = a*4
#   s = a*a
#   d = a*(2**0.5)
#   return print(p, s, round(d, 2))

# square(5)

# 3. Пользователь делает вклад в размере a рублей сроком на years лет под 10% годовых (каждый год размер его вклада увеличивается на 10%. Эти деньги прибавляются к сумме вклада, и на них в следующем году тоже будут проценты). Написать функцию bank, принимающая аргументы a и years, и возвращающую сумму, которая будет на счету пользователя.

# def bank(a, years):
#   for i in range(years):
#     a += a*0.1
#   return a

# print(f"По окончании вклада сумма на счете составит: {bank(100000, 2)} ед.")
