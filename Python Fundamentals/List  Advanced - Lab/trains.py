# Задача 2:

number_of_wagons = int(input())

train = [0] * number_of_wagons

command = input().split()

while command[0] != "End":

    if command[0] == "add":
        people = int(command[1])

        train[-1] += people

    elif command[0] == "insert":
        index = int(command[1])
        people = int(command[2])

        train[index] += people

    elif command[0] == "leave":
        index = int(command[1])
        people = int(command[2])

        train[index] -= people

    command = input().split()

print(train)