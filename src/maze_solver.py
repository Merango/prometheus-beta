from typing import List
from collections import deque

def shortest_path_maze(grid: List[List[int]]) -> int:
    """
    Find the shortest path in a 2D grid maze from top-left to bottom-right.
    
    Args:
        grid (List[List[int]]): A 2D grid where 0 represents open paths and 1 represents walls
    
    Returns:
        int: Length of the shortest path or -1 if no path exists
    
    Raises:
        ValueError: If the grid is empty or not a valid square grid
    """
    # Validate input grid
    if not grid or not grid[0]:
        raise ValueError("Grid cannot be empty")
    
    n = len(grid)
    
    # Validate grid is square and contains only 0s and 1s
    if any(len(row) != n for row in grid):
        raise ValueError("Grid must be a square NxN matrix")
    
    if any(cell not in {0, 1} for row in grid for cell in row):
        raise ValueError("Grid must contain only 0s and 1s")
    
    # Check if start or end is blocked
    if grid[0][0] == 1 or grid[n-1][n-1] == 1:
        return -1
    
    # Possible moves: right, down, left, up
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    # BFS setup
    queue = deque([(0, 0, 1)])  # (row, col, path_length)
    visited = set([(0, 0)])
    
    while queue:
        row, col, path_length = queue.popleft()
        
        # Reached bottom-right
        if row == n - 1 and col == n - 1:
            return path_length
        
        # Try all 4 directions
        for dx, dy in directions:
            new_row, new_col = row + dx, col + dy
            
            # Check if new position is valid
            if (0 <= new_row < n and 
                0 <= new_col < n and 
                grid[new_row][new_col] == 0 and 
                (new_row, new_col) not in visited):
                
                queue.append((new_row, new_col, path_length + 1))
                visited.add((new_row, new_col))
    
    # No path found
    return -1