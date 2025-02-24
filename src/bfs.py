from collections import deque
from typing import Dict, List, Optional, Set, TypeVar, Callable

T = TypeVar('T')

def breadth_first_search(graph: Dict[T, List[T]], start: T, 
                          visit: Optional[Callable[[T], bool]] = None) -> List[T]:
    """
    Perform Breadth-First Search on a graph.

    Args:
        graph (Dict[T, List[T]]): Adjacency list representation of the graph.
        start (T): Starting node for the BFS traversal.
        visit (Optional[Callable[[T], bool]], optional): Optional visitor function 
                 that can stop the search. Defaults to None.

    Returns:
        List[T]: Nodes visited during the BFS traversal.

    Raises:
        ValueError: If the start node is not in the graph.
    """
    # Validate input
    if start not in graph:
        raise ValueError(f"Start node {start} not found in graph")

    # Initialize data structures
    visited = set()
    traversal_order = []
    queue = deque([start])
    
    # BFS traversal
    while queue:
        current = queue.popleft()
        
        # Skip already visited nodes
        if current in visited:
            continue
        
        # Mark as visited
        visited.add(current)
        traversal_order.append(current)
        
        # Optional visitor function check
        if visit and visit(current):
            break
        
        # Add unvisited neighbors to queue
        for neighbor in graph.get(current, []):
            if neighbor not in visited:
                queue.append(neighbor)
    
    return traversal_order