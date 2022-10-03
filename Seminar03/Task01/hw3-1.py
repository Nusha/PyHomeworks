# Задайте список, состоящий из произвольных чисел, количество задаёт пользователь.
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётных позициях(не индексах).
# in
# 5
# out
# [10, 2, 3, 8, 9]
# 22

import random


def make_random_list_in_size(number):
    mylist = []
    for i in range(number):
        mylist.append(random.randint(1, 10))
    return mylist


def find_odd_summ_in_list(list):
    i = 0
    summ = 0
    while i < len(list):
        summ += list[i]
        i += 2
    return summ


try:
    num = int(input("Input amount of numbers : "))
    if num < 1:
        print("Incorrect amount of numbers. Mast be at least - one.")
    else:
        mylist = make_random_list_in_size(num)
        print(mylist)
        print(find_odd_summ_in_list(mylist))
except ValueError:
    print("Error. Please, input only integers.")
