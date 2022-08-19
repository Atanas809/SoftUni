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
