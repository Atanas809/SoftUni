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
