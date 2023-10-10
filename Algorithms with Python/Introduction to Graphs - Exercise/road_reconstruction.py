def dfs(node, graph, visited):
    if visited[node]:
        return

    visited[node] = True

    for child in graph[node]:
        dfs(child, graph, visited)


nodes_count = int(input())
edges_count = int(input())
graph = [[] for _ in range(nodes_count)]
edges = []

for _ in range(edges_count):
    source, destination = [int(x) for x in input().split(" - ")]
    graph[source].append(destination)
    graph[destination].append(source)
    edges.append((min(source, destination), max(source, destination)))

print("Important streets:")
for source, destination in edges:
    graph[source].remove(destination)
    graph[destination].remove(source)

    visited = [False] * nodes_count
    dfs(0, graph, visited)

    if not all(visited):
        print(f"{source} {destination}")

    graph[source].append(destination)
    graph[destination].append(source)



"""
5
5
1 - 0
0 - 2
2 - 1
0 - 3
3 - 4
"""