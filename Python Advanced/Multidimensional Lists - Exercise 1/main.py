# Test input:
"""
4
8 3 2 5
6 4 7 9
9 9 3 6
6 8 1 2
1,2 2,1 2,0
"""


def cells(matrix):
    return [x for row in matrix for x in row if x > 0]
