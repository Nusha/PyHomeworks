# 1. Напишите программу, удаляющую из текста все слова, содержащие "абв". В тексте используется разделитель пробел.
# in
# Number of words: 10
# out
# авб абв бав абв вба бав вба абв абв абв
# авб бав вба бав вба
#
# in
# Number of words: 6
# out
# ваб вба абв ваб бва абв
# ваб вба ваб бва
#
# in
# Number of words: -1
# out
# The data is incorrect

import random


def make_rand_list(n):
    my_list = []
    a = ['абв', 'авб', 'бав', 'бва', 'ваб', 'вба']
    [my_list.append(random.choice(a)) for i in range(0, n)]
    return my_list


def clear_list(inlist):
    [inlist.remove('абв') for i in inlist if 'абв' in inlist]
    return inlist


n = int(input("Number of words: "))

if n < 2:
    print('The data is incorrect')
else:
    print(' '.join(make_rand_list(n)))
    firstlist = make_rand_list(n)
    print(' '.join(clear_list(firstlist)))