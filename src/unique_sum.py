def sum_unique_elements(arr):
    """
    Calculate the sum of unique elements in the given array.
    
    Args:
        arr (list): A list of integers to process.
    
    Returns:
        int: The sum of unique elements in the array.
    
    Raises:
        TypeError: If the input is not a list or contains non-integer elements.
    
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    # Check input type
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Check if all elements are integers
    if not all(isinstance(x, int) for x in arr):
        raise TypeError("All elements must be integers")
    
    # Use a set to track unique elements efficiently
    unique_elements = set()
    unique_sum = 0
    
    for num in arr:
        # If the number is not in the set, add it to both set and sum
        if num not in unique_elements:
            unique_elements.add(num)
            unique_sum += num
        # If the number is already in the set, remove it to exclude from sum
        else:
            unique_elements.remove(num)
            unique_sum -= num
    
    return unique_sum