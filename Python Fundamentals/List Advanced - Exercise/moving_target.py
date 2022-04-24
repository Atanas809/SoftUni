def shooting():

    targets = list(map(int, input().split()))

    command = input().split()

    while command[0] != "End":

        if command[0] == "Shoot":
            index = int(command[1])
            power = int(command[2])

            if 0 <= index <= len(targets) - 1:
                if targets[index] - power <= 0:
                    targets.pop(index)
                else:
                    targets[index] -= power

        elif command[0] == "Add":
            index = int(command[1])
            value = int(command[2])

            if 0 <= index <= len(targets) - 1:
                targets.insert(index, value)

            else:
                print("Invalid placement!")

        elif command[0] == "Strike":
            index = int(command[1])
            radius = int(command[2])

            if 0 <= index - radius and index + radius <= len(targets) - 1:
                r_side = targets[:index - radius]
                l_side = targets[index + radius + 1:]

                targets = r_side + l_side

            else:
                print("Strike missed!")

        command = input().split()

    targets = list(map(str, targets))

    print("|".join(targets))

shooting()
