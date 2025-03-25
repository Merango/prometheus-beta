import heapq
from typing import List, Tuple, Callable, Any, Optional

class Node:
    """
    Represents a node in the A* search algorithm.
    
    Attributes:
        state: The current state of the node
        g_cost: Cost from start node to current node
        h_cost: Estimated cost from current node to goal
        parent: Parent node in the path
    """
    def __init__(self, state: Any, g_cost: float = 0, h_cost: float = 0, parent: Optional['Node'] = None):
        self.state = state
        self.g_cost = g_cost
        self.h_cost = h_cost
        self.parent = parent
    
    @property
    def f_cost(self) -> float:
        """Total estimated cost (g_cost + h_cost)"""
        return self.g_cost + self.h_cost
    
    def __lt__(self, other: 'Node') -> bool:
        """Allow comparison for priority queue"""
        return self.f_cost < other.f_cost
    
    def __eq__(self, other: object) -> bool:
        """Check if nodes represent the same state"""
        if not isinstance(other, Node):
            return False
        return self.state == other.state

def astar_search(
    start: Any, 
    goal_test: Callable[[Any], bool], 
    successors: Callable[[Any], List[Tuple[Any, float]]], 
    heuristic: Callable[[Any], float]
) -> Optional[List[Any]]:
    """
    Perform A* search to find the optimal path from start to goal.
    
    Args:
        start: Starting state
        goal_test: Function to check if a state is the goal
        successors: Function to generate next possible states and their costs
        heuristic: Function to estimate cost to goal
    
    Returns:
        Optimal path from start to goal, or None if no path exists
    """
    # Create start node
    start_node = Node(start, g_cost=0, h_cost=heuristic(start))
    
    # Priority queue to store nodes to explore
    frontier = []
    heapq.heappush(frontier, start_node)
    
    # Keep track of explored states to avoid revisiting
    explored = set()
    
    while frontier:
        # Get the node with lowest f_cost
        current_node = heapq.heappop(frontier)
        
        # Check if we've reached the goal
        if goal_test(current_node.state):
            return reconstruct_path(current_node)
        
        # Mark current state as explored
        explored.add(current_node.state)
        
        # Explore successors
        for (next_state, step_cost) in successors(current_node.state):
            # Skip already explored states
            if next_state in explored:
                continue
            
            # Calculate costs
            g_cost = current_node.g_cost + step_cost
            h_cost = heuristic(next_state)
            
            # Create successor node
            successor = Node(
                next_state, 
                g_cost=g_cost, 
                h_cost=h_cost, 
                parent=current_node
            )
            
            # Check if this is a better path to the state
            if not any(node.state == successor.state and node.f_cost <= successor.f_cost for node in frontier):
                heapq.heappush(frontier, successor)
    
    # No path found
    return None

def reconstruct_path(node: Node) -> List[Any]:
    """
    Reconstruct the path from start to goal.
    
    Args:
        node: Final node in the path
    
    Returns:
        List of states from start to goal
    """
    path = []
    while node:
        path.append(node.state)
        node = node.parent
    return list(reversed(path))