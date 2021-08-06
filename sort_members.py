import csv 

my_members = input("your group's csv file: ")
other_group_members = input('another group\'s csv file: ')

my_d = []
another_d = []
clear_members_list = []

with open(my_members, 'r', encoding='utf-8') as m:
    my_data = csv.reader(m, delimiter=',')

    for i in my_data:
        my_d.append(i)


with open(other_group_members, 'r', encoding='utf-8') as s:
    another_data = csv.reader(s, delimiter=',')

    for i in another_data:
        another_d.append(i)

del my_d[0]
del another_d[0]

my_d_id = [j[0] for j in my_d if j[0] ]
another_d_id = [i[0] for i in another_d if i[0]]

my = set(my_d_id)
another = set(another_d_id)

clear_data = another-my


with open('clear_members_list.csv', 'w', encoding='utf-8') as w:
    ww = csv.writer(w)

    for i in clear_data:
        d = [ ]
        d.append(i)
        ww.writerow(d)

    

