houses = list(map(int, input().split("@")))

command = input().split()

current_house = 0

while command[0] != "Love!":

    length = int(command[1])

    if current_house + length <= len(houses) - 1:
        current_house += length

        if houses[current_house] - 2 >= 0:
             houses[current_house] -= 2
             if houses[current_house] == 0:
