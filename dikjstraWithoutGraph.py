import heapq

def dijkstra(graph, start):
    # Priority queue to select the node with the smallest distance
    pq = []
    # Distance dictionary to store the shortest distance to each node
    distances = {node: float('inf') for node in graph}
    # Parent dictionary to reconstruct the shortest path
    parent = {node: None for node in graph}
    
    # Distance to the start node is 0
    distances[start] = 0
    heapq.heappush(pq, (0, start))  # (distance, node)

    while pq:
        current_distance, current_node = heapq.heappop(pq)
        
        # Skip processing if the distance in pq is outdated
        if current_distance > distances[current_node]:
            continue

        # Explore all neighbors of the current node
        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight
            
            # If a shorter path to the neighbor is found
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                parent[neighbor] = current_node
                heapq.heappush(pq, (distance, neighbor))
    
    return distances, parent


def reconstruct_path(parent, start, end):
    """Reconstructs the path from start to end using the parent dictionary."""
    path = []
    current = end
    while current is not None:
        path.append(current)
        current = parent[current]
    path.reverse()
    return path


# Example usage:
if __name__ == "__main__":
    # Graph represented as an adjacency list
    # Node -> [(neighbor, weight), ...]
    graph = {
        'A': [('B', 1), ('C', 4)],
        'B': [('A', 1), ('C', 2), ('D', 6)],
        'C': [('A', 4), ('B', 2), ('D', 3)],
        'D': [('B', 6), ('C', 3)],
    }

    start = 'A'
    end = 'D'
    
    distances, parent = dijkstra(graph, start)
    
    print("Shortest distances from start:", distances)
    print(f"Shortest path from {start} to {end}:", reconstruct_path(parent, start, end))
