def status(phones, name):
    print("-" * 20)
    print(f"Your contacts in {name}'s phonebook:")

    if len(phones.keys()) == 0:
        print(f"You don't have any contacts now, please add some and then come back here!")
        add_contact(phones, name)
    else:
        print("%" * 20)
        for key, value in phones.items():
            print(f"{key} --> {value}")
        print("%" * 20)

        
def add_contact(phones, name_of_book):
    print("*" * 20)
    name = input("Enter a contact name: ")
    phone_number = input("Enter a phone number: ")

    if name not in phones.keys():
        phones[name] = phone_number
        print("-" * 20)
        print(f"Added new contact: {name} -> {phone_number}")
        print("-" * 20)
        what_do_you_want = input("(A) for add contact"
                                 "\n(S) for phonebook status"
                                 "\nEnter your choice: ").upper()
        if what_do_you_want == "A":
            add_contact(phones, name_of_book)
        elif what_do_you_want == "S":
            status(phones, name_of_book)
    else:
        print("-" * 20)
        print(f"Contact already added")

        
def contact_book():
    phones = dict()
    name_of_contact_book = input("Enter your phonebook name: ")
