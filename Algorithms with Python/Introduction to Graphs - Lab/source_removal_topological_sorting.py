def find_dependencies(graph):
    output = {}
    for k, v in graph.items():
        if k not in output:
            output[k] = 0
        for child in v:
            if child not in output:
                output[child] = 1
            else:
                output[child] += 1

    return output


def remove_non_dependecy_node(dependencies_by_node):
    for node, dependencies in dependencies_by_node.items():
        if dependencies == 0:
            return node


nodes = int(input())
graph = {}

for _ in range(nodes):
    line_input = input().split("->")
    node = line_input[0].strip()
    graph[node] = line_input[1].strip().split(", ") if line_input[1].strip() else []


dependencies_by_node = find_dependencies(graph)
cycle = False
sorted_nodes = []

while dependencies_by_node:
    node_to_remove = remove_non_dependecy_node(dependencies_by_node)
    if node_to_remove is None:
        cycle = True
        break

    dependencies_by_node.pop(node_to_remove)
    sorted_nodes.append(node_to_remove)
    childs = graph[node_to_remove]

    for child in childs:
        dependencies_by_node[child] -= 1

if cycle:
    print("Invalid topological sorting")
else:
    print(f"Topological sorting: {', '.join(sorted_nodes)}")

"""
6
A -> B, C
B -> D, E
C -> F
D -> C, F
E -> D
F -> 
"""