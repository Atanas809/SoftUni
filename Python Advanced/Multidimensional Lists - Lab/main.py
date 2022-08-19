# Test input:
"""
3
ABC
DEF
X!@
!
"""


def symbol_in_matrix(matrix, symbol):

    is_find = False

    for row in range(len(matrix)):
        if symbol in matrix[row]:
            print(f"({row}, {matrix[row].index(symbol)})")
            is_find = True
            break

    if not is_find:
        print(f"{symbol} does not occur in the matrix")


def my_matrix():

    rows = int(input())

    matrix = []

    for n in range(rows):
        my_list = [x for x in input()]
        matrix.append(my_list)

    searched_symbol = input()

    symbol_in_matrix(matrix, searched_symbol)
