import string


# Test input:
"""
4 6
"""

rows, columns = [int(x) for x in input().split()]
matrix = []
lowercase = string.ascii_lowercase

for row in range(rows):
    result = []
    for column in range(row, columns + row):
        current_result = lowercase[row] + lowercase[column] + lowercase[row]
        result.append(current_result)
    matrix.append(result)
