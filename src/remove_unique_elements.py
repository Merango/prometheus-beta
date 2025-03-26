def remove_unique_elements(my_list):
    """
    Remove unique (non-duplicate) elements from a list of integers.
    
    This function uses only built-in list methods to filter out elements 
    that appear only once in the input list, keeping only elements 
    that have multiple occurrences.
    
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
    
    # Iterate through the list while keeping track of seen numbers
    for num in my_list:
        # Use count() to check if the number appears more than once
        if my_list.count(num) > 1 and num not in duplicates:
            # Find all instances of duplicate number
            duplicates.extend([num] * (my_list.count(num)))
    
    # Return all duplicates to preserve order and allow multiple repeat duplicates
    return duplicates