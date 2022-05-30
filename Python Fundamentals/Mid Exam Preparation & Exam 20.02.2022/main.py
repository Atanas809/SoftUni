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
        first_last = info[1]
        num_coffees = int(info[2]) - 1
        if 0 <= num_coffees <= len(name_coffees) - 1:
            if first_last == "first":
                name_coffees = name_coffees[num_coffees + 1:]
            elif first_last == "last":
                if num_coffees == 0:
