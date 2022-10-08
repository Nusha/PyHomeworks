# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов
# исходной последовательности в том же порядке.
# in
# 7
# out
# [4, 5, 3, 3, 4, 1, 2]
# [5, 1, 2]
# in
# -1
# out
# Negative value of the number of numbers!
# []
import random
import winsound


def make_sequence(num):
    if num < 0:
        print('Negative value of the number of numbers!')
        return 'Nothing'
    else:
        mylist = [random.randint(1, 10) for i in range(num)]
        return mylist


def only_non_duplicate(any_list):
    res = []
    [res.append(element) for element in any_list if any_list.count(element) < 2]
    return res

try:
    n = int(input("Input size of list to be generated: "))
    final = make_sequence(n)
    print(final)
    print(only_non_duplicate(final))
except ValueError:
    winsound.MessageBeep()
    print(f"{chr(8252)}We're working only with integers, pls, try again.")

