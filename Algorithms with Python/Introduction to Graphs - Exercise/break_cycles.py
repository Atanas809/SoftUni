def dfs(node, destination, graph, visited):
    if node in visited:
        return

    visited.add(node)

    if node == destination:
        return
    for child in graph[node]:
        dfs(child, destination, graph, visited)


def has_cycle(node, destination, graph):
    visited = set()

    dfs(node, destination, graph, visited)

    return destination in visited


nodes = int(input())
graph = {}
edges = []
edges_to_remove = []
count = 0

for _ in range(nodes):
    source, destination_str = input().split(" -> ")
    destinations = destination_str.split(" ")
    graph[source] = destinations
    for child in destinations:
        edges.append((source, child))

for source, destination in sorted(edges, key=lambda x: (x[0], x[1])):
    if destination not in graph[source] or source not in graph[destination]:
        continue
    graph[source].remove(destination)
    graph[destination].remove(source)

    if has_cycle(source, destination, graph):
        edges_to_remove.append([source, destination])
        count += 1
    else:
        graph[source].append(destination)
        graph[destination].append(source)

print(f"Edges to remove: {count}")
for source, dest in edges_to_remove:
    print(f"{source} - {dest}")

"""
8
1 -> 2 5 4
2 -> 1 3
3 -> 2 5
4 -> 1
5 -> 1 3
6 -> 7 8
7 -> 6 8
8 -> 6 7
"""