name_coffees = input().split(" ")

number_of_commands = int(input())

for num in range(1, number_of_commands + 1):
    info = input().split(" ")
    command = info[0]
    if command == "Reverse":
