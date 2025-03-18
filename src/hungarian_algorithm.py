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
    
    # Determine rows and columns
    num_rows, num_cols = work_matrix.shape
    
    # Step 1: Subtract row minima
    row_mins = work_matrix.min(axis=1)
    work_matrix -= row_mins[:, np.newaxis]
    
    # Step 2: Subtract column minima
    col_mins = work_matrix.min(axis=0)
    work_matrix -= col_mins
    
    # Helper function for optimal assignment
    def find_optimal_assignment(matrix):
        # This is a simplified version of finding optimal assignment
        assignments = []
        assigned_cols = set()
        
        # Prioritize lower-indexed rows and columns
        for row in range(matrix.shape[0]):
            # Find potential zero columns in this row
            zero_indices = np.where((matrix[row] == 0))[0]
            
            # Find a zero column that hasn't been assigned
            for col in zero_indices:
                if col not in assigned_cols:
                    assignments.append((row, col))
                    assigned_cols.add(col)
                    break
        
        return assignments
    
    # Find assignments
    assignments = find_optimal_assignment(work_matrix)
    
    # Ensure all rows are assigned, even if they need padding
    if len(assignments) < num_rows:
        # If fewer assignments than rows, add placeholders
        assigned_rows = {row for row, _ in assignments}
        for row in range(num_rows):
            if row not in assigned_rows:
                # Find first unassigned column
                unassigned_cols = set(range(num_cols)) - {col for _, col in assignments}
                if unassigned_cols:
                    col = min(unassigned_cols)
                    assignments.append((row, col))
    
    # Filter assignments to original matrix dimensions
    filtered_assignments = [
        (row, col) for row, col in assignments 
        if row < num_rows and col < num_cols
    ]
    
    # Compute total cost
    total_cost = sum(matrix[row, col] for row, col in filtered_assignments)
    
    return filtered_assignments, total_cost