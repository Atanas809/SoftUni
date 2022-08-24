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
