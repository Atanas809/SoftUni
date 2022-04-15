# Задача 10:
def output(coins, energy):

    print("Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")

def bakery():
    energy = 100
    coins = 100

    info = input().split("|")

    is_closed = False

    for x in info:

        if is_closed:
            break

        data = x.split("-")

        command = data[0]
        number = int(data[1])

        if command == "rest":

            if energy + number > 100:
                print("You gained 0 energy.")
            else:
                energy += number
                print(f"You gained {number} energy.")

            print(f"Current energy: {energy}.")

        elif command == "order":
            if energy - 30 >= 0:
                energy -= 30
                coins += number
                print(f"You earned {number} coins.")
            else:
                energy += 50
                print("You had to rest!")

        else:
            if coins - number >= 0:
                coins -= number
                print(f"You bought {command}.")
            else:
                print(f"Closed! Cannot afford {command}.")
                is_closed = True
                break

    if not is_closed:
        output(coins, energy)

bakery()