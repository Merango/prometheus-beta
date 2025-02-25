class KnightsTour:
    """
    A class to solve the Knight's Tour problem on an 8x8 chessboard.
    
    The Knight's Tour is a sequence of moves of a knight on a chessboard such that 
    the knight visits every square exactly once.
    """
    
    def __init__(self, board_size=8):
        """
        Initialize the Knight's Tour solver.
        
        :param board_size: Size of the chessboard (default is 8x8)
        """
        self.board_size = board_size
        self.moves = [
            (2, 1), (1, 2), (-1, 2), (-2, 1),
            (-2, -1), (-1, -2), (1, -2), (2, -1)
        ]
    
    def is_valid_move(self, board, x, y):
        """
        Check if the move is valid (within board and not previously visited).
        
        :param board: Current state of the chessboard
        :param x: x-coordinate of the move
        :param y: y-coordinate of the move
        :return: Boolean indicating if the move is valid
        """
        return (0 <= x < self.board_size and 
                0 <= y < self.board_size and 
                board[x][y] == -1)
    
    def solve(self, start_x, start_y):
        """
        Solve the Knight's Tour problem starting from a given position.
        
        :param start_x: Starting x-coordinate
        :param start_y: Starting y-coordinate
        :return: 2D list representing the order of moves, or None if no solution
        """
        # Validate input
        if not (0 <= start_x < self.board_size and 0 <= start_y < self.board_size):
            raise ValueError("Starting position is out of board bounds")
        
        # Initialize board with -1 (unvisited)
        board = [[-1 for _ in range(self.board_size)] for _ in range(self.board_size)]
        
        # Mark the starting position
        board[start_x][start_y] = 0
        
        # Try to solve using backtracking
        if self._solve_tour(board, start_x, start_y, 1):
            return board
        
        return None
    
    def _solve_tour(self, board, x, y, move_count):
        """
        Recursive backtracking method to solve the Knight's Tour.
        
        :param board: Current state of the chessboard
        :param x: Current x-coordinate
        :param y: Current y-coordinate
        :param move_count: Number of moves made so far
        :return: Boolean indicating if a complete tour is found
        """
        # If all squares are visited, tour is complete
        if move_count == self.board_size * self.board_size:
            return True
        
        # Try all possible knight moves
        for dx, dy in self.moves:
            next_x, next_y = x + dx, y + dy
            
            # Check if the next move is valid
            if self.is_valid_move(board, next_x, next_y):
                # Mark the next square with current move count
                board[next_x][next_y] = move_count
                
                # Recursively try to complete the tour
                if self._solve_tour(board, next_x, next_y, move_count + 1):
                    return True
                
                # Backtrack if the move doesn't lead to a solution
                board[next_x][next_y] = -1
        
        return False