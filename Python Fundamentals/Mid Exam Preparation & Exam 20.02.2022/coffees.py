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
                    name_coffees.remove(name_coffees[-1])
                else:
                    num_coffees = - num_coffees
                    name_coffees = name_coffees[:num_coffees]
    elif command == "Prefer":
        index1 = int(info[1])
        index2 = int(info[2])
        if 0 <= index1 <= len(name_coffees) - 1 and 0 <= index2 <= len(name_coffees) - 1:
            name_coffees[index1], name_coffees[index2] = name_coffees[index2], name_coffees[index1]

print("Coffees:")
print(' '.join(name_coffees))
