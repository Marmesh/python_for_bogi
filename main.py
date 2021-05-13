from pprint import pprint
import csv
new_contacts = []

with open("bogi_quest.csv") as f:
    rows = csv.reader(f, delimiter=";")
    contacts_list = list(rows)
print('Начальный лист')
pprint(contacts_list)


while len(contacts_list) > 0:
    check = 0
    index_list = []
    for items in contacts_list:
        if contacts_list[0][0] == items[0]:
            check += 1
            index_list.append(contacts_list.index(items))
    if check == 1:
        new_contacts.append(contacts_list[0])
        contacts_list.pop(0)
    else:
        get_list = [contacts_list[0][0], '', '']
        for index in index_list:

            if (contacts_list[index][1] != '') and (get_list[1] == ''):
                get_list[1] = contacts_list[index][1]
            if (contacts_list[index][2] != '') and (get_list[2] == ''):
                get_list[2] = contacts_list[index][2]
        new_contacts.append(get_list)
        for index in reversed(index_list):
            contacts_list.pop(index)
    # print(contacts_list[i][0])
print('По-крастоте лист')
pprint(new_contacts)
