# Задача 3:

def chars_in_range():

    start = input()
    end = input()

    for x in range(ord(start) + 1, ord(end)):
        print(chr(x), end = " ")

chars_in_range()