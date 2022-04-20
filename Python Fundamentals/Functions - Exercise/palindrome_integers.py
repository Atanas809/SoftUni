# Задача 8:

def palindrome():

    numbers = input().split(", ")

    for x in numbers:
        if x == x[::-1]:
            print("True")
        else:
            print("False")

palindrome()
