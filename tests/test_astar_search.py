import pytest
import sys
import os

# Add the project root to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.astar_search import astar_search

def test_simple_grid_path():
    """Test A* search on a simple grid-like problem."""
    def successors(state):
        """Generate possible moves in a grid."""
        x, y = state
        moves = [
            ((x+1, y), 1),   # right
            ((x-1, y), 1),   # left
            ((x, y+1), 1),   # up
            ((x, y-1), 1)    # down
        ]
        return moves
    
    def heuristic(state):
        """Manhattan distance heuristic."""
        goal = (4, 4)
        return abs(state[0] - goal[0]) + abs(state[1] - goal[1])
    
    start = (0, 0)
    goal = (4, 4)
    
    def goal_test(state):
        return state == goal
    
    path = astar_search(start, goal_test, successors, heuristic)
    
    assert path is not None, "Path should exist"
    assert path[0] == start, "Path should start at start state"
    assert path[-1] == goal, "Path should end at goal state"

def test_no_path_exists():
    """Test scenario where no path exists."""
    def successors(state):
        """No valid moves."""
        return []
    
    def heuristic(state):
        """Constant heuristic."""
        return 0
    
    start = 'A'
    
    def goal_test(state):
        return state == 'B'
    
    path = astar_search(start, goal_test, successors, heuristic)
    
    assert path is None, "Should return None when no path exists"

def test_start_is_goal():
    """Test when start state is the goal state."""
    def successors(state):
        """No moves needed."""
        return []
    
    def heuristic(state):
        """Zero heuristic."""
        return 0
    
    start = 'A'
    
    def goal_test(state):
        return state == start
    
    path = astar_search(start, goal_test, successors, heuristic)
    
    assert path == [start], "Should return path with just the start/goal state"

def test_complex_path_finding():
    """Test a more complex path-finding scenario."""
    # Simplified graph-like problem
    graph = {
        'A': [('B', 4), ('C', 2)],
        'B': [('D', 3)],
        'C': [('D', 1)],
        'D': [('E', 2)],
        'E': []
    }
    
    def successors(state):
        """Generate graph moves."""
        return graph.get(state, [])
    
    def heuristic(state):
        """Simple heuristic to prefer moving towards goal."""
        goal_order = ['A', 'B', 'C', 'D', 'E']
        return len(goal_order) - goal_order.index(state)
    
    start = 'A'
    
    def goal_test(state):
        return state == 'E'
    
    path = astar_search(start, goal_test, successors, heuristic)
    
    assert path is not None, "Path should exist"
    assert path[0] == start, "Path should start at start state"
    assert path[-1] == 'E', "Path should end at goal state"
    # Optimal path could be A -> C -> D -> E
    assert len(path) <= 4, "Path should be reasonably short"