# Для чисел в пределах от 20 до N найти числа, кратные 20 или 21. Use comprehension.


#

def find_multipl(n):
    lst = list(range(n + 1))
    lst2 = []
    [lst2.append(lst[i]) for i in range(1, len(lst)) if lst[i] % 20 == 0 or lst[i] % 21 == 0]
    return lst2


try:
    num = int(input('Input N: '))
    print(find_multipl(num)) if num >= 20 else print(f'{chr(8505)} You are to enter numbers from 20.')
except ValueError:
    print(f'{chr(10060)} Please input only integers.')
