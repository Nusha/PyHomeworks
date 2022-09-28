import math
try:
    xa = int(input("Input Xa coordinate: "))
    ya = int(input("Input Ya coordinate: "))
    xb = int(input("Input Xb coordinate: "))
    yb = int(input("Input Yb coordinate: "))
    ab = math.sqrt((xb-xa)**2+(yb-ya)**2)
    print(ab.__round__(3))
except ValueError:
    print("Please enter only integers as values.")
