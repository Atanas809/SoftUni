def output(houses, index):
    
    print(f"Cupid's last position was {index}.")
    
    if sum(houses) != 0:
        count = 0
        for x in houses:
            if x != 0:
                count += 1
        print(f"Cupid has failed {count} places.")
    else:
        print("Mission was successful.")

def valentines_day():

    houses = list(map(int, input().split("@")))

    command = input().split()

    index = 0

    while command[0] != "Love!":

        jump = int(command[1])

        if index + jump <= len(houses) - 1:
            index += jump

            if houses[index] == 0:
                print(f"Place {index} already had Valentine's day.")
            elif houses[index] - 2 >= 0:
                houses[index] -= 2
                if houses[index] == 0:
                    print(f"Place {index} has Valentine's day.")

        else:
            index = 0

            if houses[index] == 0:
                print(f"Place {index} already had Valentine's day.")
            elif houses[index] - 2 >= 0:
                houses[index] -= 2
                if houses[index] == 0:
                    print(f"Place {index} has Valentine's day.")

        command = input().split()

    output(houses, index)

valentines_day()
