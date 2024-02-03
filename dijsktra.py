import heapq
import networkx as nx


def dijkstra(graph, start):
    priority_queue = [(0, start)]
    heapq.heapify(priority_queue)
    visited = set()
    distances = {vertex: float("infinity") for vertex in graph.nodes}
    distances[start] = 0

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        if current_vertex in visited:
            continue

        visited.add(current_vertex)

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight["weight"]

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances


graph = nx.Graph()

graph.add_edge("A", "B", weight=2)
graph.add_edge("A", "C", weight=4)
graph.add_edge("B", "D", weight=7)
graph.add_edge("C", "E", weight=5)
graph.add_edge("D", "E", weight=1)

start_vertex = "A"

shortest_paths = dijkstra(graph, start_vertex)

for vertex, distance in shortest_paths.items():
    print(f"Найкоротша відстань від {start_vertex} до {vertex}: {distance}")
