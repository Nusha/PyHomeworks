# Вычислить число c заданной точностью d
# in
# Enter a real number: 9
# Enter the required accuracy '0.0001': 0.000001
# out
# 9.000000
# in
# Enter a real number: 8.98785
# Enter the required accuracy '0.0001': 0.001
# out
# 8.988

import winsound
import decimal


def accurate_number(number, accuracy):
    res = number.quantize(accuracy)
    return res


try:
    num = decimal.Decimal(float(input(f'Enter {chr(8477)} number: ').replace(',', '.')))
    d = decimal.Decimal(input('Enter the required accuracy "0.0001": ').replace(',', '.'))
    print(accurate_number(num, d))
except ValueError:
    winsound.PlaySound('SystemHand', winsound.SND_ALIAS)
    r = '\033[31m'
    print(f"{chr(9940)} {r}Error. Please enter only real numbers. ',' or '.' are allowed to use as delimiters.")
except decimal.InvalidOperation:
    winsound.PlaySound('SystemHand', winsound.SND_ALIAS)
    r = '\033[31m'
    print(f"{chr(10071)} {r}Error in decimal module. Please enter only real, float, not symbols numbers. ',' or '.' "
          f"are allowed to use as delimiters.")
