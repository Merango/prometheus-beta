def bead_sort(arr):
    """
    Implement the Bead Sort (Gravity Sort) algorithm for positive integers.
    
    Bead Sort is a natural sorting algorithm that works by simulating physical 
    beads dropping under gravity, creating a unique visualization of sorting.
    
    Args:
        arr (list): A list of non-negative integers to be sorted.
    
    Returns:
        list: A sorted list of integers in ascending order.
    
    Raises:
        ValueError: If the input contains negative numbers.
        TypeError: If the input is not a list or contains non-integer elements.
    """
    # Validate input
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Check for non-integer or negative elements
    if any(not isinstance(x, int) or x < 0 for x in arr):
        raise ValueError("All elements must be non-negative integers")
    
    # Handle empty or single-element list
    if len(arr) <= 1:
        return arr.copy()
    
    # Find the maximum element to determine the number of beads
    max_val = max(arr)
    
    # Create a column for each input number representing its value
    beads = [[1] * x + [0] * (max_val - x) for x in arr]
    
    # Simulate gravity sorting
    for j in range(max_val):
        # Count number of beads in this row
        col_beads = sum(row[j] for row in beads)
        
        # Update columns from bottom to top
        for i in range(len(beads)):
            beads[i][j] = 1 if j < col_beads else 0
    
    # Reconstruct the sorted array
    sorted_arr = [sum(row) for row in beads]
    
    return sorted_arr