# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# in -> out
# - 6782 -> 23
# - 0.67 -> 13
# - 198.45 -> 27

def numbers_summ(number):
    power: int = pow(10, len(number) - 1)
    number = float(number)
    number *= power
    res: int = 0
    while number:
        res = res + number % 10
        number = number // 10
    return int(res)


try:
    num = input("Input value: ")
    print(numbers_summ(num))

except ValueError:
    print("Pls, input correct value: float or integer.")
