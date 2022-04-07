correct_number = 23
print("Enter number:", end = " ")
number = int(input())
while number != correct_number:
    print("Wrong number!")
    print("Try another one:", end = " ")
    number = int(input())
if number == correct_number:
    print("You won!")
