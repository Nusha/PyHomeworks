# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
try:
    x, y, z = input("Введите x, y, z:  ").split()
    print("True" if not(x or y or z) == (not x and not y and not z) else "False")
except ValueError:
    print("Pls, input any value!")

# Solution using for loop to check all values,  presented at the seminar.
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             if not(x or y or z) == (not x and not y and not z):
#                 print(x, y, z)
