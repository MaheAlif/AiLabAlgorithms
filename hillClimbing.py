import matplotlib.pyplot as plt
import networkx as nx
import random

def hill_climbing(graph, start, goal, heuristic):
    """
    Performs the Hill Climbing Search Algorithm.
    
    Args:
        graph: The adjacency list of the graph where each node connects to neighbors with weights.
        start: The starting node.
        goal: The goal node.
        heuristic: A dictionary mapping nodes to their heuristic values.

    Returns:
        path: The path from start to goal (if found).
        visited: The list of visited nodes.
    """
    current = start
    path = [current]
    visited = [current]
    
    while current != goal:
        # Get neighbors of the current node
        neighbors = graph.get(current, [])
        
        # If no neighbors, terminate
        if not neighbors:
            print("No path exists.")
            return None, visited
        
        # Select the best neighbor based on heuristic values
        best_neighbor = None
        best_heuristic = float('inf')
        for neighbor, _ in neighbors:
            if neighbor not in visited and heuristic[neighbor] < best_heuristic:
                best_neighbor = neighbor
                best_heuristic = heuristic[neighbor]
        
        # If no better neighbor is found, terminate (local maximum reached)
        if best_neighbor is None or best_heuristic >= heuristic[current]:
            print("Stuck at a local maximum.")
            return None, visited
        
        # Move to the best neighbor
        current = best_neighbor
        path.append(current)
        visited.append(current)
    
    return path, visited


def visualize_hill_climbing(graph, path, visited):
    """
    Visualizes the graph, visited nodes, and the path found using matplotlib and networkx.
    
    Args:
        graph: The adjacency list of the graph.
        path: The path found (if any).
        visited: The list of visited nodes.
    """
    G = nx.DiGraph()
    
    # Add edges to the graph
    for node, neighbors in graph.items():
        for neighbor, weight in neighbors:
            G.add_edge(node, neighbor, weight=weight)
    
    # Node positions for visualization
    pos = nx.spring_layout(G, seed=42)
    
    # Draw nodes and edges
    nx.draw(G, pos, with_labels=True, node_size=700, node_color="lightblue", font_weight="bold", edge_color="gray")
    
    # Highlight visited nodes
    nx.draw_networkx_nodes(G, pos, nodelist=visited, node_color="yellow", node_size=800)
    
    # Highlight the path
    if path:
        path_edges = list(zip(path, path[1:]))
        nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color="red", width=2)
        nx.draw_networkx_nodes(G, pos, nodelist=path, node_color="green", node_size=800)
    
    # Draw edge weights
    edge_labels = nx.get_edge_attributes(G, "weight")
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    
    # Display the graph
    plt.title("Hill Climbing Search Visualization")
    plt.show()


# Example usage
if __name__ == "__main__":
    # Define the graph as an adjacency list
    # Node -> [(neighbor, weight), ...]
    graph = {
        'A': [('B', 1), ('C', 4)],
        'B': [('D', 2), ('E', 6)],
        'C': [('F', 3)],
        'D': [('G', 1)],
        'E': [('G', 1), ('H', 5)],
        'F': [('H', 2)],
        'G': [('I', 1)],
        'H': [('I', 2)],
        'I': []
    }

    # Define heuristic values for each node
    heuristic = {
        'A': 10,
        'B': 8,
        'C': 9,
        'D': 6,
        'E': 7,
        'F': 8,
        'G': 4,
        'H': 5,
        'I': 0  # Goal node has a heuristic of 0
    }

    start = 'A'
    goal = 'H'

    # Perform Hill Climbing Search
    path, visited = hill_climbing(graph, start, goal, heuristic)

    # Print the results
    if path:
        print("Path found:", path)
    else:
        print("No path found.")
    print("Visited nodes:", visited)
    
    # Visualize the graph and the search process
    visualize_hill_climbing(graph, path, visited)
