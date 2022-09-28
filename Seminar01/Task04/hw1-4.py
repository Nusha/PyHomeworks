# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек
# в этой четверти (x и y).
try:
    q = int(input("Input number of quarter: "))
    if q == 1:
        print("x > 0, y > 0")
    elif q == 2:
        print("x < 0, y > 0")
    elif q == 3:
        print("x < 0, y < 0")
    elif q == 4:
        print("x > 0, y < 0")
    else:
        print("The quarter is entered incorrectly")
except ValueError:
    print("Error. Please enter correct value: integer 1-4.")
