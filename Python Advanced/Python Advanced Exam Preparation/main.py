def next_player(current_player):
    if current_player == 1:
        return 0

    return 1


def move():
    command = input()
    command = command.replace("(", "")
    command = command.replace(")", "")
    command = command.replace(",", " ")
    row, col = [int(x) for x in command.split()]

    return row, col
