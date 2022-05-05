# Задача 4:
def output(counter, contacts):

    for x in range(counter):
        searched_name = input()

        if searched_name not in contacts.keys():
            print(f"Contact {searched_name} does not exist.")
        else:
            print(f"{searched_name} -> {contacts[searched_name]}")

def phonebook():

    info = input().split("-")

    contacts = dict()

    while not info[0].isdigit():

        name = info[0]
        phone = info[1]

        contacts[name] = phone

        info = input().split("-")

    output(int(info[0]), contacts)

phonebook()

