def reverse_matrix_elements(matrix):
    """
    Reverse the elements of each cell in an N x N matrix.
    
    Args:
        matrix (List[List[int]]): A square matrix of integers 
    
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
    
    # Validate matrix size
    if rows < 1 or rows > 1000:
        raise ValueError("Matrix size must be between 1 and 1000")
    
    # Create a new matrix with reversed elements
    reversed_matrix = []
    for row in matrix:
        # Validate each element in the row
        for num in row:
            if not isinstance(num, int) or num < 0:
                raise ValueError("Matrix elements must be non-negative integers")
            
            # Additional validation for range of possible reversible digits
            str_num = str(num)
            if len(str_num) > 10:  # Practical limit to prevent integer overflow
                raise ValueError("Matrix elements must be integers within a reasonable range")
        
        # Reverse each element in the row, handling multi-digit numbers
        # Use integer conversion to remove leading zeros
        reversed_row = [int(str(abs(num))[::-1]) for num in row]
        reversed_matrix.append(reversed_row)
    
    return reversed_matrix