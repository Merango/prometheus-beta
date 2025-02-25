import pytest
import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from knights_tour import KnightsTour

def test_knights_tour_initialization():
    """Test the initialization of KnightsTour class."""
    kt = KnightsTour()
    assert kt.board_size == 8
    assert len(kt.moves) == 8

def test_is_valid_move():
    """Test the is_valid_move method."""
    kt = KnightsTour()
    
    # Create a board with some visited squares
    board = [[-1 for _ in range(8)] for _ in range(8)]
    board[3][3] = 0  # Mark a square as visited
    
    # Test valid moves
    assert kt.is_valid_move(board, 5, 4) == True
    assert kt.is_valid_move(board, 1, 2) == True
    
    # Test invalid moves (out of bounds)
    assert kt.is_valid_move(board, -1, 0) == False
    assert kt.is_valid_move(board, 8, 8) == False
    
    # Test invalid moves (already visited)
    board[5][4] = 1
    assert kt.is_valid_move(board, 5, 4) == False

def test_solve_invalid_start():
    """Test solving with invalid starting positions."""
    kt = KnightsTour()
    
    # Test out of bounds starting positions
    with pytest.raises(ValueError):
        kt.solve(-1, 0)
    with pytest.raises(ValueError):
        kt.solve(8, 8)

def test_solve_complete_tour():
    """Test that a complete Knight's Tour is found."""
    kt = KnightsTour()
    
    # Try solving from different starting positions
    for start_x in [0, 3, 7]:
        for start_y in [0, 3, 7]:
            solution = kt.solve(start_x, start_y)
            
            # Check if a solution was found
            assert solution is not None
            
            # Verify the solution
            moves = set()
            for row in solution:
                for val in row:
                    moves.add(val)
            
            # Check that all squares are visited exactly once
            assert len(moves) == kt.board_size * kt.board_size
            assert 0 in moves and kt.board_size * kt.board_size - 1 in moves

def test_solve_move_sequence():
    """Verify the move sequence properties."""
    kt = KnightsTour()
    solution = kt.solve(0, 0)
    
    assert solution is not None
    
    # Check that moves are valid knight moves
    def is_knight_move(x1, y1, x2, y2):
        dx = abs(x1 - x2)
        dy = abs(y1 - y2)
        return (dx == 1 and dy == 2) or (dx == 2 and dy == 1)
    
    last_pos = None
    for x in range(kt.board_size):
        for y in range(kt.board_size):
            current_val = solution[x][y]
            if last_pos is not None:
                last_x, last_y = last_pos
                assert is_knight_move(last_x, last_y, x, y), f"Invalid move from {last_pos} to {(x, y)}"
            last_pos = (x, y)