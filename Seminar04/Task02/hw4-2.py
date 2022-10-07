# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# Простые делители числа
# in
# 54
# out
# [2, 3, 3, 3]
# in
# 9990
# out
# [2, 3, 3, 3, 5, 37]
# in
# 650
# out
# [2, 5, 5, 13]
import winsound


def get_multipiers(number):
    i = 2
    result = []
    while i * i <= number:
        while number % i == 0:
            result.append(i)
            number //= i
        i += 1
    if number > 1:
        result.append(number)
    return result


try:
    num = int(input('Input N: '))
    if num == 1:
        print('1 is empty product')
    elif num <= 0:
        print(f'{num} is not positive integer')
    else:
        print(get_multipiers(num))
except ValueError:
    winsound.MessageBeep()
    print(f'{chr(10060)} Error.Please input only positive integers.')
