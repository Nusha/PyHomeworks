# Реализуйте алгоритм перемешивания списка. Без функции shuffle из модуля random.
# 10
# -> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# -> [0, 7, 6, 3, 4, 2, 9, 5, 1, 8]
import random

def make_my_list(num):
    mylist = []
    for i in range(num):
        mylist.append(i)
    return mylist


def my_shuffle(mylist):
    for i in range(len(mylist)):
        j = (random.randint(0, len(mylist)-1))
        tmp = mylist[j]
        mylist[j] = mylist[i]
        mylist[i] = tmp
    return mylist

try:
    size = int(input("Enter list size: "))

    nlist = make_my_list(size)
    print(nlist)
    print(my_shuffle(nlist))
except ValueError:
    print("Please input only integers.")
