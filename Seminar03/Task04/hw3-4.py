# Задайте список из произвольных вещественных чисел, количество задаёт пользователь.
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# in
# 5
# out
# [5.16, 8.62, 6.57, 7.92, 9.22]
# Min: 0.16, Max: 0.92. Difference: 0.76
import random


def generate_float_list(size):
    floatlist = []
    for i in range(size):
        floatlist.append(random.uniform(1.00, 9.99).__round__(2))
    return floatlist


def reformat_list(relist):
    for i in range(len(relist)):
        relist[i] = round(relist[i] - int(relist[i]), 2)
        i += i
    return relist


try:
    num = int(input("Input size of list: "))
    if num < 1:
        print("You can't input value less then 1.")
    else:
        first_list = generate_float_list(num)
        print(first_list)
        mylist = reformat_list(first_list)
        res = round(max(mylist) - min(mylist), 2)
        print(f"Min: {min(mylist)}, Max: {max(mylist)}, Difference: {res}")
except ValueError:
    print("Error. Pls, input only integers.")
