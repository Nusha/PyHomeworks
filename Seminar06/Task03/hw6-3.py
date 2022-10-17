# Написать функцию, аргументы имена сотрудников, возвращает словарь, ключи — первые буквы имён, значения — списки,
# содержащие имена, начинающиеся с соответствующей буквы.

from itertools import groupby


def names_to_dict(inlist):
    dicti = {}
    for k, g in groupby(inlist, key=lambda x: x[0]):
        if k in dicti:
            dicti[k] += g
        else:
            dicti[k] = list(g)
    return dicti


names = sorted(["Иван", "Мария", "Петр", "Илья", "Марина", "Петр", "Алина", "Бибочка"])
print(names)
print(names_to_dict(names))
