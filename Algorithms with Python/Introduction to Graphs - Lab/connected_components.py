def dfs(node, graph, visited, result):
    if visited[node]:
        return

    visited[node] = True

    for child in graph[node]:
        dfs(child, graph, visited, result)

    result.append(node)


nodes = int(input())
graph = []

for _ in range(nodes):
    line = input()
    graph.append([int(x) for x in line.split(" ")] if line else [])

visited = [False] * nodes

for node in range(len(graph)):
    if visited[node]:
        continue
    result = []
    dfs(node, graph, visited, result)
    print(f"Connected component: {' '.join(str(x) for x in result)}")


"""
9
3 6
3 4 5 6
8
0 1 5
1 6
1 3
0 1 4

2
"""