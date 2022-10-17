# Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
# Use comprehension.

from random import randint as rnd


def generate_list_in():
    lin = []
    [lin.append(rnd(1, 25)) for i in range(0, 9)]
    return lin


def find_bigger_elements(lin):
    lout = []
    [lout.append(lin[i]) for i in range(1, len(lin)) if lin[i] > lin[i - 1]]
    return lout


lst = generate_list_in()
print(lst)
print(find_bigger_elements(lst))
