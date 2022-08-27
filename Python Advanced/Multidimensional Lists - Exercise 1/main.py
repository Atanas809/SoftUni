from collections import deque

# Test input:
"""
5 6
SoftUni
"""

rows, columns = [int(x) for x in input().split()]

text = deque(input())

matrix = []

for row in range(rows):
