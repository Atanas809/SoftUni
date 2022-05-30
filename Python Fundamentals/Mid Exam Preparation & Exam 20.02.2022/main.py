name_coffees = input().split(" ")

number_of_commands = int(input())

for num in range(1, number_of_commands + 1):
    info = input().split(" ")
    command = info[0]
    if command == "Reverse":
        name_coffees.reverse()
    elif command == "Include":
        current_coffee = info[1]
        name_coffees.append(current_coffee)
    elif command == "Remove":
