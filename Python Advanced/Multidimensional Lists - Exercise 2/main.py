# Задача 1:

# Test input:
"""
1 2 3 |4 5 6 |  7  88
"""

data = input().split("|")
matrix = []

for x in range(len(data) - 1, -1, -1):

      current_data = data[x].strip()
    current_column = current_data.split()
    matrix.extend(current_column)

print(*matrix, sep=" ")
