# Test input:
"""
5
. A . . 1
R . 2 . .
4 7 . 1 .
. . . 2 .
. 3 . . .
down
right
left
down
up
left
"""


def moves(row, col, direction):

    possible_moves = {
        "up": [row - 1, col],
        "down": [row + 1, col],
        "right": [row, col + 1],
        "left": [row, col - 1],
    }

    for key, value in possible_moves.items():
        if key == direction:
            return value


size = int(input())

matrix = []
alice_row = 0
alice_col = 0

for row in range(size):
    current_col = [x for x in input().split()]
    if "A" in current_col:
        alice_row = row
        alice_col = current_col.index("A")
    matrix.append(current_col)

tea_bags = 0

while True:
    current_dir = input()

    next_row, next_col = moves(alice_row, alice_col, current_dir)
