# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Без использования встроенной функции преобразования, без строк.


def return_bin_number(number):
    bin_number = []
    while number > 0:
        bin_number.insert(0, number % 2)
        number = number // 2
    return bin_number


try:
    num = int(input("Input number: "))

    if num < 0:
        print("-", *return_bin_number(abs(num)), sep="")
    else:
        print(*return_bin_number(num), sep="")
except ValueError:
    print('Error. Please input only integers.')
