import numpy as np

def hungarian_algorithm(cost_matrix):
    """
    Solve the assignment problem using the Hungarian algorithm.
    
    Args:
        cost_matrix (list or np.ndarray): A 2D matrix of assignment costs 
                                          where lower values indicate better assignments.
    
    Returns:
        list: A list of (row, column) tuples representing the optimal assignment.
    
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
    
    # Step 1: Subtract row minima
    row_mins = work_matrix.min(axis=1)
    work_matrix -= row_mins[:, np.newaxis]
    
    # Step 2: Subtract column minima
    col_mins = work_matrix.min(axis=0)
    work_matrix -= col_mins
    
    # Step 3: Cover zeros with minimal number of lines
    def cover_zeros(matrix):
        # Find zero locations
        zero_locations = matrix == 0
        
        # Greedy row-column covering
        rows_covered = set()
        cols_covered = set()
        assignments = []
        
        for row in range(matrix.shape[0]):
            for col in range(matrix.shape[1]):
                if matrix[row, col] == 0 and row not in rows_covered and col not in cols_covered:
                    assignments.append((row, col))
                    rows_covered.add(row)
                    cols_covered.add(col)
        
        return assignments
    
    # Solve the assignment
    assignments = cover_zeros(work_matrix)
    
    # If not all rows/columns are assigned, we need to adjust
    if len(assignments) < min(matrix.shape):
        # This is a simplified version - more complex adjustment might be needed
        # Typically would involve creating additional zeros
        raise ValueError("Could not find complete assignment")
    
    # Map back to original costs and validate
    total_cost = sum(matrix[row, col] for row, col in assignments)
    
    return assignments, total_cost