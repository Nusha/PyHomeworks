import operations as op
import menu as m
import csv

ch = 1
pb = [['John Dow', '1234567', 'john@doe.com']]
while ch in (1, 2, 3, 4, 5, 6, 7):
    ch = m.menu()
    if ch == 1:
        pb = op.add_contact(pb)
    elif ch == 2:
        pb = op.remove_contact(pb)
    elif ch == 3:
        d = op.search_contact(pb)
        if d == -1:
            print("The contact does not exist. Please try again")
    elif ch == 4:
        op.display_all(pb)
    elif ch == 5:
        op.save_to_file(pb)
    elif ch == 6:
        pb = op.read_from_file()
    else:
        print('Bye')
        break
