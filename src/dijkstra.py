import heapq
from typing import Dict, List, Tuple, Optional

def dijkstra(graph: Dict[str, Dict[str, int]], start: str) -> Tuple[Dict[str, int], Dict[str, Optional[str]]]:
    """
    Implement Dijkstra's algorithm to find the shortest paths from a start node.
    
    Args:
        graph (Dict[str, Dict[str, int]]): A graph represented as an adjacency list 
                                           where keys are nodes and values are dictionaries 
                                           of neighboring nodes and their edge weights.
        start (str): The starting node for path calculation.
    
    Returns:
        Tuple containing:
        - A dictionary of shortest distances from the start node to all other nodes
        - A dictionary of previous nodes for path reconstruction
    
    Raises:
        ValueError: If the start node is not in the graph
    """
    # Validate input
    if start not in graph:
        raise ValueError(f"Start node '{start}' not found in the graph")
    
    # Initialize distances and previous nodes
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    previous_nodes = {node: None for node in graph}
    
    # Priority queue to store nodes to visit
    pq = [(0, start)]
    
    while pq:
        current_distance, current_node = heapq.heappop(pq)
        
        # Skip if we've found a shorter path already
        if current_distance > distances[current_node]:
            continue
        
        # Check if current node's neighbors can be improved
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            
            # Update if a shorter path is found
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor] = current_node
                heapq.heappush(pq, (distance, neighbor))
    
    return distances, previous_nodes

def reconstruct_path(previous_nodes: Dict[str, Optional[str]], start: str, end: str) -> List[str]:
    """
    Reconstruct the shortest path between start and end nodes.
    
    Args:
        previous_nodes (Dict[str, Optional[str]]): Dictionary of previous nodes 
                                                   from Dijkstra's algorithm
        start (str): The starting node
        end (str): The destination node
    
    Returns:
        List[str]: The shortest path from start to end
    
    Raises:
        ValueError: If no path exists between start and end
    """
    path = []
    current = end
    
    # Reconstruct path backwards
    while current is not None:
        path.append(current)
        current = previous_nodes[current]
        
        # Check for unreachable node
        if current is None and path[-1] != start:
            raise ValueError(f"No path exists between {start} and {end}")
    
    # Reverse path to get correct order
    return list(reversed(path))