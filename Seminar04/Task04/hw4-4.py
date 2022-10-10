# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (от 0 до 10) многочлена, записать в
# файл полученный многочлен не менее 3-х раз.
# in
# 9
# 5
# 3
#
# out in the file
# 3*x^9 + 3*x^8 - 2*x^6 + 1*x^5 - 3*x^4 - 3*x^2 + 3 = 0
# 4*x^5 + 1*x^4 - 3*x^3 - 3 = 0
# 4*x^2 - 4 = 0


from random import choice


def polynomial(num: int):
    if num < 1:
        return 0

    poly = ""
    num_list = range(0, 10)

    with open("poly.txt", "a", encoding="utf-8") as my_f:
        for i in range(num, 0, -1):
            value = choice(num_list)
            if value:
                poly += f"{value}*x^{i} {choice('+-')} "

        my_f.write(f"{poly}{choice(num_list)} = 0\n")


for _ in range(3):
    polynomial(int(input()))

