first_number = int(input())
second_number = int(input())
operator = input()

result = 0

if operator == "+":
    result = first_number + second_number
    if result % 2 == 0:
        print(f"{first_number} {operator} {second_number} = {result} - even")
    else:
        print(f"{first_number} {operator} {second_number} = {result} - odd")
elif operator == "-":
    result = first_number - second_number
    if result % 2 == 0:
        print(f"{first_number} {operator} {second_number} = {result} - even")
    else:
        print(f"{first_number} {operator} {second_number} = {result} - odd")
elif operator == "*":
    result = first_number * second_number
    if result % 2 == 0:
        print(f"{first_number} {operator} {second_number} = {result} - even")
    else:
        print(f"{first_number} {operator} {second_number} = {result} - odd")
elif operator == "/":
    if second_number == 0:
        print(f"Cannot divide {first_number} by zero")
    else:
        result = first_number / second_number
        print(f"{first_number} {operator} {second_number} = {result:.2f}")
elif operator == "%":
    if second_number == 0:
        print(f"Cannot divide {first_number} by zero")
    else:
        result = first_number % second_number
        print(f"{first_number} {operator} {second_number} = {result}")
