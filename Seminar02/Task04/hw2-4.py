# Напишите программу, которая принимает на вход 2 числа. Задайте список из N элементов, заполненных числами из
# промежутка [-N, N]. Найдите произведение элементов на указанных позициях(не индексах).
# Position one: 1
# Position two: 3
# Number of elements: 5
# -> [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
# -> 15

def make_list_elem(numele):
    listelem = []
    for i in range(-numele, numele + 1):
        listelem.append(i)
    return listelem


try:
    pos_1 = int(input("Input position 1: "))
    pos_2 = int(input("Input position 2: "))
    num = int(input("Number of elements: "))

    if pos_1 > (num * 2 + 1) or pos_2 > (num * 2 + 1) or pos_1 <= 0 >= pos_2:
        print(f"Error. Index out of range, position 1 and position 2 must be in range from 1 to {num * 2 + 1}. ")
    else:
        print(make_list_elem(num))
        le = make_list_elem(num)
        print(abs(le[pos_1 - 1] * le[pos_2 - 1]))

except ValueError:
    print("Error. Please input only integer.")
