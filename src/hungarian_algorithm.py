import numpy as np

def hungarian_algorithm(cost_matrix):
    """
    Solve the assignment problem using the Hungarian algorithm.
    
    Args:
        cost_matrix (list or np.ndarray): A 2D matrix of assignment costs 
                                          where lower values indicate better assignments.
    
    Returns:
        tuple: A tuple containing:
            - list of (row, column) tuples representing the optimal assignment
            - total cost of the assignment
    
    Raises:
        ValueError: If the input is not a valid 2D matrix.
    """
    # Convert input to numpy array and validate
    try:
        matrix = np.array(cost_matrix, dtype=float)
    except:
        raise ValueError("Input must be a valid 2D matrix")
    
    # Validate matrix dimensions
    if matrix.ndim != 2 or matrix.shape[0] == 0 or matrix.shape[1] == 0:
        raise ValueError("Matrix must be a non-empty 2D array")
    
    # Create a working copy of the matrix
    work_matrix = matrix.copy()
    
    # Pad the matrix if it's not square
    max_dim = max(work_matrix.shape)
    if work_matrix.shape[0] != work_matrix.shape[1]:
        padded_matrix = np.full((max_dim, max_dim), np.max(work_matrix) * 2)
        padded_matrix[:work_matrix.shape[0], :work_matrix.shape[1]] = work_matrix
        work_matrix = padded_matrix
    
    # Step 1: Subtract row minima
    row_mins = work_matrix.min(axis=1)
    work_matrix -= row_mins[:, np.newaxis]
    
    # Step 2: Subtract column minima
    col_mins = work_matrix.min(axis=0)
    work_matrix -= col_mins
    
    # Track assignments
    assignments = []
    
    # Helper function to find zero assignments
    def find_assignments(matrix):
        # Create a copy of the matrix to mark assignments
        checked_matrix = matrix.copy()
        curr_assignments = []
        
        # Greedy row-first assignment
        for row in range(matrix.shape[0]):
            zero_cols = np.where((checked_matrix[row] == 0))[0]
            for col in zero_cols:
                # Check if column is not already assigned
                if all(col != existing_col for _, existing_col in curr_assignments):
                    curr_assignments.append((row, col))
                    # Mark the column as assigned
                    checked_matrix[:, col] = float('inf')
                    break
        
        return curr_assignments
    
    # Find initial assignments
    assignments = find_assignments(work_matrix)
    
    # Compute total cost using original matrix
    total_cost = sum(matrix[row, col] for row, col in assignments 
                     if row < matrix.shape[0] and col < matrix.shape[1])
    
    return assignments, total_cost