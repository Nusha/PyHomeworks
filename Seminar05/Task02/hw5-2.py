# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.Входные и выходные данные хранятся
# в отдельных текстовых файлах.

from itertools import groupby


def encode_file(file_src, file_rle):
    with open(file_src) as my_f_1, \
            open(file_rle, "a") as my_f_2:
        string = ''.join(my_f_1.readlines())
        [list(g) for k, g in groupby(string)]
        my_f_2.write(''.join(['{}{}'.format(sum(1 for _ in g), k) for k, g in groupby(string)]))


def decode_file(file_rle, file_res):
    with open(file_rle) as my_f_1, \
            open(file_res, "a") as my_f_2:
        string = ''.join(my_f_1.readlines())
        decode = ''
        count = ''
        for char in string:
            if char.isdigit():
                count += char
            else:
                decode += char * int(count)
                count = ''
        my_f_2.write(decode)


file_in = "text_words.txt"
file_out = "text_code_words.txt"
file_r = "result.txt"

encode_file(file_in, file_out)
decode_file(file_out, file_r)
