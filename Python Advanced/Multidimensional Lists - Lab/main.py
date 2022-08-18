# Test input:
"""
3, 6
7, 1, 3, 3, 2, 1
1, 3, 9, 8, 5, 6
4, 6, 7, 9, 1, 0
"""

rows, columns = [int(x) for x in input().split(", ")]

matrix = []

total_sum = 0

for n in range(rows):
    my_list = [int(x) for x in input().split(", ")]
    matrix.append(my_list)
