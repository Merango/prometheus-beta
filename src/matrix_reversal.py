def reverse_matrix_elements(matrix):
    """
    Reverse the elements of each cell in an N x N matrix.
    
    Args:
        matrix (List[List[int]]): A square matrix of integers in range [0, 9]
    
    Returns:
        List[List[int]]: A new matrix with each element reversed
    
    Raises:
        ValueError: If the matrix is not square or contains invalid elements
    """
    # Validate input matrix
    if not matrix or not matrix[0]:
        raise ValueError("Matrix cannot be empty")
    
    # Check if matrix is square
    rows = len(matrix)
    if any(len(row) != rows for row in matrix):
        raise ValueError("Matrix must be square")
    
    # Validate matrix size and elements
    if rows < 1 or rows > 1000:
        raise ValueError("Matrix size must be between 1 and 1000")
    
    # Create a new matrix with reversed elements
    reversed_matrix = []
    for row in matrix:
        # Validate row elements
        if any(not (0 <= num <= 9) for num in row):
            raise ValueError("Matrix elements must be integers in range [0, 9]")
        
        # Reverse each element in the row
        reversed_row = [int(str(num)[::-1]) for num in row]
        reversed_matrix.append(reversed_row)
    
    return reversed_matrix