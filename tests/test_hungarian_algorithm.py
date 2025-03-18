import pytest
import numpy as np
from src.hungarian_algorithm import hungarian_algorithm

def test_basic_assignment():
    """Test a basic assignment problem with a small matrix."""
    cost_matrix = [
        [1, 2, 3],
        [2, 4, 6],
        [3, 6, 9]
    ]
    assignments, total_cost = hungarian_algorithm(cost_matrix)
    
    # Validate assignments
    assert len(assignments) == 3
    assert set(assignments) == {(0, 0), (1, 1), (2, 2)}
    
    # Validate total cost (sum of min cost assignments)
    expected_cost = cost_matrix[0][0] + cost_matrix[1][1] + cost_matrix[2][2]
    assert total_cost == expected_cost

def test_rectangular_matrix():
    """Test assignment with rectangular matrix."""
    cost_matrix = [
        [1, 2, 3, 4],
        [2, 4, 6, 8],
        [3, 6, 9, 12]
    ]
    assignments, total_cost = hungarian_algorithm(cost_matrix)
    
    # Validate assignments
    assert len(assignments) == 3
    
    # Validate total cost
    total_computed_cost = sum(cost_matrix[row][col] for row, col in assignments)
    assert total_cost == total_computed_cost

def test_invalid_input():
    """Test error handling for invalid inputs."""
    # Empty matrix
    with pytest.raises(ValueError):
        hungarian_algorithm([])
    
    # Non-2D input
    with pytest.raises(ValueError):
        hungarian_algorithm([1, 2, 3])
    
    # Non-numeric input
    with pytest.raises(ValueError):
        hungarian_algorithm([['a', 'b'], ['c', 'd']])

def test_single_row_col_matrix():
    """Test assignment with single row/column matrix."""
    # Single row matrix
    cost_matrix_row = [[1, 2, 3]]
    assignments, total_cost = hungarian_algorithm(cost_matrix_row)
    assert len(assignments) == 1
    assert total_cost == 1  # Minimum cost element
    
    # Single column matrix
    cost_matrix_col = [[1], [2], [3]]
    assignments, total_cost = hungarian_algorithm(cost_matrix_col)
    assert len(assignments) == 1
    assert total_cost == 1  # Minimum cost element

def test_symmetric_matrix():
    """Test assignment with symmetric cost matrix."""
    cost_matrix = [
        [10, 15, 20],
        [15, 20, 25],
        [20, 25, 30]
    ]
    assignments, total_cost = hungarian_algorithm(cost_matrix)
    
    # Validate unique assignments
    rows, cols = zip(*assignments)
    assert len(set(rows)) == len(rows)
    assert len(set(cols)) == len(cols)
    
    # Validate total cost
    computed_cost = sum(cost_matrix[row][col] for row, col in assignments)
    assert total_cost == computed_cost