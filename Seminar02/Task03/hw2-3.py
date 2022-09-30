# Задайте список из n чисел, заполненный по формуле (1 + 1/n) ** n и выведите на экран их сумму.
# Для n = 6: [2, 2, 2, 2, 2, 3] -> 13


def sum_of_list(num):
    numlist = []
    for i in range(1, num + 1):
        numlist.append(round((1 + 1 / i) ** i))
    return numlist


try:
    n = int(input("Input N  "))
    print(f"{sum_of_list(n)} -> {sum(sum_of_list(n))}")
except ValueError:
    print("Pls, enter only integer")
