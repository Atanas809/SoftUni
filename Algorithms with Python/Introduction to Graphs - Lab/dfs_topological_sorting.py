from collections import deque


def dfs(node, visited, cycles, sorted_nodes):
    if node in cycles:
        raise Exception("Cycle detected.")
    if node in visited:
        return

    visited.add(node)
    cycles.add(node)

    for child in graph[node]:
        dfs(child, visited, cycles, sorted_nodes)

    cycles.remove(node)
    sorted_nodes.appendleft(node)


nodes = int(input())
graph = {}

for _ in range(nodes):
    line_input = input().split("->")
    node = line_input[0].strip()
    graph[node] = line_input[1].strip().split(", ") if line_input[1].strip() else []

visited = set()
cycles = set()
sorted_nodes = deque()

for node in graph:
    dfs(node, visited, cycles, sorted_nodes)

print(f"Topological sorting: {', '.join(sorted_nodes)}")
