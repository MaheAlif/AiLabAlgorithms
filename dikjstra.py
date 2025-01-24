import heapq
import matplotlib.pyplot as plt
import networkx as nx


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


def visualize_graph(graph, shortest_path=None):
    """Visualizes the graph and highlights the shortest path."""
    # Create a directed graph using networkx
    G = nx.DiGraph()
    
    # Add edges and weights to the graph
    for node, neighbors in graph.items():
        for neighbor, weight in neighbors:
            G.add_edge(node, neighbor, weight=weight)
    
    # Node positions for visualization
    pos = nx.spring_layout(G, seed=42)
    
    # Draw nodes and edges
    nx.draw(G, pos, with_labels=True, node_size=700, node_color="lightblue", font_weight="bold", edge_color="gray")
    
    # Draw edge labels (weights)
    edge_labels = nx.get_edge_attributes(G, "weight")
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    
    # Highlight the shortest path
    if shortest_path:
        path_edges = list(zip(shortest_path, shortest_path[1:]))
        nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color="red", width=2)
        nx.draw_networkx_nodes(G, pos, nodelist=shortest_path, node_color="red", node_size=800)
    
    # Display the graph
    plt.title("Graph Visualization")
    plt.show()


# Example usage
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
    
    # Run Dijkstra's algorithm
    distances, parent = dijkstra(graph, start)
    
    # Find the shortest path from start to end
    shortest_path = reconstruct_path(parent, start, end)
    
    print("Shortest distances from start:", distances)
    print(f"Shortest path from {start} to {end}:", shortest_path)
    
    # Visualize the graph
    visualize_graph(graph, shortest_path)
