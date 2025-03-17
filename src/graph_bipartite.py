from typing import List, Dict

def is_bipartite(graph: List[List[int]]) -> bool:
    """
    Check if a graph is bipartite using a two-coloring approach.

    A bipartite graph is a graph whose vertices can be divided into two 
    independent sets such that every edge connects a vertex in one set 
    to a vertex in the other set.

    Args:
        graph (List[List[int]]): An adjacency list representation of the graph.
                                 Each index represents a node, and the list at 
                                 that index contains its adjacent nodes.

    Returns:
        bool: True if the graph is bipartite, False otherwise.

    Raises:
        ValueError: If the graph is empty or None.
    """
    # Check for invalid input
    if not graph:
        raise ValueError("Graph cannot be empty")

    # Initialize color array
    colors = [0] * len(graph)

    # Helper function for depth-first coloring
    def color_graph(node: int, color: int) -> bool:
        # Color the current node
        colors[node] = color

        # Check adjacent nodes
        for neighbor in graph[node]:
            # If neighbor not colored, color with opposite color
            if colors[neighbor] == 0:
                if not color_graph(neighbor, -color):
                    return False
            # If neighbor has same color, graph is not bipartite
            elif colors[neighbor] == color:
                return False
        
        return True

    # Check each uncolored node
    for node in range(len(graph)):
        if colors[node] == 0:
            # Start coloring from this node
            if not color_graph(node, 1):
                return False

    return True