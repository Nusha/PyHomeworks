# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

def neg_fib(n):
    if n == 0 or n == 1:
        return n
    elif n == -1:
        return 1
    elif n < 0:
        if n % 2 == 0:
            s = -1
        else:
            s = 1
        return s * neg_fib(-n)
    else:
        return neg_fib(n - 1) + neg_fib(n - 2)


def make_seq_list(n):
    n = n * -1
    seq_list = []
    for i in range(n, -n + 1):
        seq_list.append(neg_fib(n))
        n += 1
    return seq_list


try:
    num = int(input("Please enter positive number for fibonacci sequence: "))
    if num < 0:
        print("Error. Pls, only positive numbers.")
    else:
        print(make_seq_list(num))
except ValueError:
    print("Error. Only integers allowed.")
