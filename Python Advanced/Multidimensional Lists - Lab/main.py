# Test input:
"""
3, 6
7 1 3 3 2 1
1 3 9 8 5 6
4 6 7 9 1 0
"""


def output(columns_sum):

    print(*columns_sum, sep="\n")


def my_matrix():

    rows, columns = [int(x) for x in input().split(", ")]

    columns_sum = [0] * columns

    for n in range(rows):
