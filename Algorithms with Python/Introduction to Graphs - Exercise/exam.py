import heapq

def dijkstra(graph, start, end, closed_roads):
    distances = {city: float('inf') for city in graph}
    distances[start] = 0

    queue = [(0, start)]

    while queue:
        distance, current_city = heapq.heappop(queue)

        if current_city == end:
            break

        if distance > distances[current_city]:
            continue

        for neighbor, edge_distance in graph[current_city].items():
            first_edge = f"{current_city}-{neighbor}"
            second_edge = f"{neighbor}-{current_city}"
            if first_edge in closed_roads or second_edge in closed_roads:
                continue

            new_distance = distance + edge_distance
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                heapq.heappush(queue, (new_distance, neighbor))

    path = []
    current_city = end

    while current_city != start:
        path.append(current_city)
        for neighbor, edge_distance in graph[current_city].items():
            if distances[current_city] == distances[neighbor] + edge_distance:
                current_city = neighbor
                break

    path.append(start)
    path.reverse()
    return path, distances[end]


n = int(input())
graph = {}
for _ in range(n):
    road_data = input().split(" - ")
    city1, city2, distance = road_data[0], road_data[1], int(road_data[2])
    if city1 not in graph:
        graph[city1] = {}
    if city2 not in graph:
        graph[city2] = {}
    graph[city1][city2] = distance
    graph[city2][city1] = distance

closed_roads_data = input()
closed_roads = closed_roads_data.split(",")

start_city = input()
end_city = input()

path, total_distance = dijkstra(graph, start_city, end_city, closed_roads)

print(" - ".join(path))
print(total_distance)


"""
8
A - B - 2
A - C - 4
B - C - 1
B - D - 4
C - D - 3
C - E - 5
D - E - 2
B - E - 1
B-D
A
E
"""

"""
8
A - B - 2
A - C - 4
B - C - 1
B - D - 4
C - D - 3
C - E - 5
D - E - 2
B - E - 1
B-E
A
E
"""