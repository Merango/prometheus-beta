def remove_unique_elements(my_list):
    """
    Remove unique (non-duplicate) elements from a list of integers.
    
    This function uses only built-in list methods to filter out elements 
    that appear only once in the input list, keeping only elements 
    that have multiple occurrences, preserving their original order.
    
    Args:
        my_list (list): A list of integers to process
    
    Returns:
        list: A new list containing only the duplicate elements
    
    Examples:
        >>> remove_unique_elements([1, 2, 3, 2, 4, 1, 5])
        [1, 2, 2, 1]
        >>> remove_unique_elements([1, 2, 3, 4, 5])
        []
        >>> remove_unique_elements([])
        []
    """
    # Return an empty list if input list is empty
    if not my_list:
        return []
    
    # Create a new list to store duplicate elements
    duplicates = []
    
    # Iterate through the list in order
    for i, num in enumerate(my_list):
        # Find how many times this exact element appears before this index
        duplicate_count = my_list[:i+1].count(num)
        
        # If this is a duplicate AND it appears exactly when we want it to
        if my_list.count(num) > 1 and duplicate_count <= 2:
            duplicates.append(num)
    
    return duplicates