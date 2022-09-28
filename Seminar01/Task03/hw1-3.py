# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти
# плоскости, в которой находится эта точка (или на какой оси она находится).
try:
    x, y = input("Input X and Y coordinates, delimited by space: ").split()
    x, y = float(x), float(y)
    if x > 0 < y:
        print("1 quarter")
    elif x < 0 < y:
        print("2 quarter")
    elif x < 0 > y:
        print("3 quarter")
    elif x > 0 > y:
        print("4 quarter")
    else:
        print("Error, 0 entered!")
except ValueError:
    print("Incorrect values entered, pls enter two numbers divided by spaces.")
