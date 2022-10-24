# Test inputs:
"""
1st:
-------------------
10 30 B 4 20 24
7 8 27 23 11 19
13 3 14 B 17 В
12 5 21 22 9 6
B 26 1 28 29 2
25 B 16 15 B 18
(1, 1)
(20, 15)
(4, 0)
--------------------

2nd:
--------------------
B 30 14 23 20 24
29 8 27 18 11 19
13 3 B B 17 6
28 5 21 22 9 B
10 B 26 12 B 2
25 1 16 15 7 4
(0, 0)
(2, 2)
(2, 3)
--------------------
"""


def prize_won(points):
    if 100 <= points <= 199:
        return "Football"
    elif 200 <= points <= 299:
        return "Teddy Bear"
    elif result >= 300:
        return "Lego Construction Set"


def sum_col_values(col, board):
    moves = {
        board[0][col],
        board[1][col],
        board[2][col],
        board[3][col],
        board[4][col],
        board[5][col],
    }

    current_result = 0

    for value in moves:
        if value.isdigit():
            value = int(value)
            current_result += value

    return current_result


def is_valid_position(row, column, size):

    if 0 <= row < size and 0 <= column < size:
        return True

    return False


size = 6

board = [input().split(" ") for _ in range(size)]

throws = [input() for _ in range(3)]

result = 0
won = False

for throw in throws:
    throw = throw.replace("(", "")
    throw = throw.replace(")", "")
    throw = throw.replace(",", "")
    throw = throw.split()
    current_row = int(throw[0])
    current_column = int(throw[1])

    if is_valid_position(current_row, current_column, size):
        if board[current_row][current_column] == "B":
            board[current_row][current_column] = "-"
            current_points = sum_col_values(current_column, board)

            result += current_points
