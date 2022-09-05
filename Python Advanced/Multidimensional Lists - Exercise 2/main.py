# Test input:
"""
5
1 3 7 9 11
X 5 4 X 63
7 3 21 95 1
B 1 73 4 9
9 2 33 2 0
"""


def is_valid(bunny_row, bunny_col, size, matrix):

    if 0 <= bunny_row < size and 0 <= bunny_col < size:
        if matrix[bunny_row][bunny_col] != "X":
            return True
    return False


size = int(input())

matrix = []

bunny_row = 0
bunny_col = 0

for row in range(size):
    current_col = [x for x in input().split()]
    if "B" in current_col:
        bunny_row = row
        bunny_col = current_col.index("B")

    matrix.append(current_col)

directions = {
