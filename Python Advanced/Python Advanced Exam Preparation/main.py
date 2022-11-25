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


size = 6

maze = []
names = input().split(", ")

for _ in range(size):
    current_row_el = [x for x in input().split(" ")]
    maze.append(current_row_el)

current_player = 0
player1 = False
player2 = False
two_player_rest = False
counter = 0

while True:
    next_move = move()
    row, col = next_move

    if not two_player_rest:
        if maze[row][col] == "E":
            print(f"{names[current_player]} found the Exit and wins the game!")
            break
        elif maze[row][col] == "T":
            other_player = names[1] if current_player == 0 else names[0]
            print(f"{names[current_player]} is out of the game! The winner is {other_player}.")
            break
        elif maze[row][col] == "W":
            print(f"{names[current_player]} hits a wall and needs to rest.")
            if current_player == 0:
                player1 = True
            elif current_player == 1:
                player2 = True

            if player1 and player2:
                two_player_rest = True
                continue
    else:
        if counter + 1 == 2:
            player1 = False
            player2 = False
            two_player_rest = False
        else:
            counter += 1

    if player1:
        current_player = 1
        continue
