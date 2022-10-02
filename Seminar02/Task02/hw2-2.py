# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# 1 - 1 * 1, 2 - 1 * 2, 3 - 1 * 2 * 3, 4 - 1 * 2 * 3 * 4 и т.д.
# - 4 -> [1, 2, 6, 24]
# - 6 -> [1, 2, 6, 24, 120, 720]


def find_fact(num):
    fact = []
    comp = 1
    for i in range(num):
        comp *= i + 1
        fact.append(comp)
    return fact


try:
    number = int(input("Input N: "))
    if number < 1:
        print("N can not be less than 1.")
    else:
        print(find_fact(number))
except:
    print("Error. Please enter only integer.")
