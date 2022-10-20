import csv


def add_contact(pb):
    dip = [str(input("Enter name: ")), int(input("Enter number: ")), str(input("Enter e-mail address: "))]
    pb.append(dip)
    return pb


def remove_contact(pb):
    query = str(
        input("Please enter the name of the contact you wish to remove: "))
    temp = 0
    for i in range(len(pb)):
        if query == pb[i][0]:
            temp += 1
            print(pb.pop(i))
            print("This query has now been removed")
            return pb
    if temp == 0:
        print("Sorry, you have entered an invalid query.\
    Please recheck and try again later.")
        return pb


def search_contact(pb):
    choice = int(input("Enter search criteria\n\
    \n1. Name\n2. Number\n3. Email-id\n\
    \nPlease enter: "))

    temp = []
    check = -1

    if choice == 1:
        query = str(
            input("Please enter the name of the contact you wish to search: "))
        for i in range(len(pb)):
            if query == pb[i][0]:
                check = i
                temp.append(pb[i])

    elif choice == 2:
        query = int(
            input("Please enter the number of the contact you wish to search: "))
        for i in range(len(pb)):
            if query == pb[i][1]:
                check = i
                temp.append(pb[i])

    elif choice == 3:
        query = str(input("Please enter the e-mail ID\
        of the contact you wish to search: "))
        for i in range(len(pb)):
            if query == pb[i][2]:
                check = i
                temp.append(pb[i])

    else:
        print("Invalid search criteria")
        return -1

    if check == -1:
        return -1

    else:
        display_all(temp)
        return check


def display_all(pb):
    if not pb:
        print("List is empty: []")
    else:
        for i in range(len(pb)):
            print(pb[i])


def save_to_file(pb):
    with open('pb.csv', 'w', encoding='utf8', newline='') as my_file:
        wr = csv.writer(my_file, quoting=csv.QUOTE_MINIMAL)
        wr.writerows(pb)


def read_from_file():
    with open('pb.csv', 'r', encoding='utf8', newline='') as my_file:
        pb = my_file.readlines()
    return pb
