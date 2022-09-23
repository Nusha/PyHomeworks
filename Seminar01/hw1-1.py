day = int(input("Input a day of the week: "))
if int(day) < 1 or int(day) > 7:
    print("Not a day of the week!")
else:
    print("Workday" if 1 <= int(day) <= 5 else "Weekend")
