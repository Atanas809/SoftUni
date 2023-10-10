def dfs(node, graph, visited):
    if visited[node] is not None:
        return visited[node]
    if len(graph[node]) == 0:
        visited[node] = 1
        return 1

    curr_result = 0
    for child in graph[node]:
        curr_result += dfs(child, graph, visited)

    visited[node] = curr_result
    return curr_result


num = int(input())
graph = [[] for _ in range(num)]
visited = {x: None for x in range(num)}
result = 0

for n in range(num):
    line = list(input())
    for idx, value in enumerate(line):
        if value == "Y":
            graph[n].append(idx)

for node in range(len(graph)):
    if visited[node] is not None:
        result += visited[node]
    else:
        result += dfs(node, graph, visited)

print(result)

"""
6
NNNNNN
YNYNNY
YNNNNY
NNNNNN
YNYNNN
YNNYNN
"""