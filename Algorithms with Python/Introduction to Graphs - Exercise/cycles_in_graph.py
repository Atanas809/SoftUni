def dfs(node, graph, visited):
    if node not in visited:
        return
    if visited[node]:
        raise Exception("Cycle detected!")

    visited[node] = True

    for child in graph[node]:
        dfs(child, graph, visited)


lines = input()
visited = {}
graph = {}

while lines != "End":
    source, destination = lines.split("-")
    if source not in graph:
        visited[source] = False
        graph[source] = []
    graph[source].append(destination)
    lines = input()


for node in graph:
    if visited[node]:
        continue
    try:
        dfs(node, graph, visited)
    except Exception:
        print("Acyclic: No")
        break
else:
    print("Acyclic: Yes")

"""
K-J
J-N
N-L
N-M
M-I
End
"""