def dfs(row, col, char, matrix, visited):
    if row < 0 or col < 0 or row >= len(matrix) or col >= len(matrix[0]):
        return
    if visited[row][col]:
        return
    if matrix[row][col] != char:
        return

    visited[row][col] = True
    dfs(row + 1, col, char, matrix, visited)
    dfs(row - 1, col, char, matrix, visited)
    dfs(row, col + 1, char, matrix, visited)
    dfs(row, col - 1, char, matrix, visited)


rows = int(input())
cols = int(input())
matrix = []
visited = []

for _ in range(rows):
    matrix.append(list(input()))
    visited.append([False] * cols)

areas = dict()
areas_count = 0
for row in range(rows):
    for col in range(cols):
        if visited[row][col]:
            continue
        char = matrix[row][col]
        dfs(row, col, char, matrix, visited)
        if char not in areas:
            areas[char] = 1
        else:
            areas[char] += 1
        areas_count += 1


print(f"Areas: {areas_count}")
for char, value in sorted(areas.items()):
    print(f"Letter '{char}' -> {value}")

"""
5
9
asssaadas
adsdasdad
sdsdadsas
sdasdsdsa
ssssasddd
"""