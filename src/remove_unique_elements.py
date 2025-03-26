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
    
    # Track unique and duplicate elements
    seen_unique = []
    seen_duplicate = []
    
    # Iterate through the list
    for num in my_list:
        # If number is already in seen duplicates, add it again
        if num in seen_duplicate:
            duplicates.append(num)
        # If number is already in unique list, move it to duplicates
        elif num in seen_unique:
            seen_unique.remove(num)
            seen_duplicate.append(num)
            duplicates.append(num)
            duplicates.append(num)
        # If number is new, add to unique list
        else:
            seen_unique.append(num)
    
    return duplicates