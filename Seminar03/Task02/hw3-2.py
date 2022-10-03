# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# in
# 4
# out
# [2, 5, 8, 10]
# [20, 40]
import random


def make_random_list(size):
    firstlist = []
    for i in range(size):
        firstlist.append(random.randrange(1, 10))
    return firstlist


def find_prod_pair_inlist(firstlist):
    secondlist = []
    k = 0
    j = len(firstlist) - 1
    while k < j:
        secondlist.append(firstlist[k] * firstlist[j])
        k = k + 1
        j = j - 1
    if j == k:
        secondlist.append(firstlist[k])
        return secondlist
    return secondlist


try:
    num = int(input("Input size: "))
    if num < 1:
        print("The value must not be less 1.")
    else:
        mylist = make_random_list(num)
        print(mylist)
        print(find_prod_pair_inlist(mylist))
except ValueError:
    print("Error. Please input only integers.")
