graph = {
    1 : [(5 , 2), (4, 7)],
    2 : [(6, 2), (1, 4), (5,17)],
    3 : [(2, 6), (5, 10), (1, 15)],
    4 : [(3, 1), (6, 2), (2, 12)],
    5 : [(4, 3), (6, 9)],
    6 : [(1, 2), (3, 18)]
}

def bellman_ford(graph, start):
    # Step 1: Initialize distances and predecessors
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    predecessors = {node: None for node in graph}

    # Step 2: Relax edges repeatedly
    for _ in range(len(graph) - 1):
        for node in graph:
            for neighbor, weight in graph[node]:
                if distances[node] + weight < distances[neighbor]:
                    distances[neighbor] = distances[node] + weight
                    predecessors[neighbor] = node

    # Step 3: Check for negative cycles
    for node in graph:
        for neighbor, weight in graph[node]:
            if distances[node] + weight < distances[neighbor]:
                raise ValueError("Graph contains a negative cycle")

    return distances, predecessors

start_node = 1
distances, predecessors = bellman_ford(graph, start_node)
print("Distances:", distances)
print("Predecessors:", predecessors)

def shortest_path(predecessors, start, end):
    path = []
    current_node = end
    while current_node != start:
        path.append(current_node)
        current_node = predecessors[current_node]
    path.append(start)
    path.reverse()
    return path

# Example usage
end_node = 6
path = shortest_path(predecessors, start_node, end_node)
print("Shortest path:", path)