import pytest
from src.maze_solver import shortest_path_maze

def test_basic_path():
    grid = [
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 0]
    ]
    assert shortest_path_maze(grid) == 4

def test_no_path_wall_start():
    grid = [
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 0]
    ]
    assert shortest_path_maze(grid) == -1

def test_no_path_wall_end():
    grid = [
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 1]
    ]
    assert shortest_path_maze(grid) == -1

def test_larger_grid():
    grid = [
        [0, 0, 0, 0],
        [1, 1, 0, 1],
        [0, 0, 0, 0],
        [0, 1, 1, 0]
    ]
    assert shortest_path_maze(grid) == 7

def test_single_cell_grid():
    grid = [[0]]
    assert shortest_path_maze(grid) == 1

def test_impossible_grid():
    grid = [
        [0, 1, 0],
        [1, 1, 1],
        [0, 0, 0]
    ]
    assert shortest_path_maze(grid) == -1

def test_empty_grid_raises_error():
    with pytest.raises(ValueError):
        shortest_path_maze([])

def test_invalid_grid_not_square():
    with pytest.raises(ValueError):
        shortest_path_maze([[0, 1], [0]])

def test_invalid_grid_values():
    with pytest.raises(ValueError):
        shortest_path_maze([[0, 2], [3, 0]])