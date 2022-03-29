# Задача 1:
needed_book = input()
checked_books = 0
is_finded = False

current_book = input()
while current_book != "No More Books":
    if needed_book != current_book:
        checked_books += 1
        current_book = input()
    else:
        is_finded = True
        break
if is_finded:
    print(f"You checked {checked_books} books and found it.")
else:
    print("The book you search is not here!")
    print(f"You checked {checked_books} books.")
