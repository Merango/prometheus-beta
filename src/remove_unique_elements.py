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
    
    # Track added elements to avoid adding duplicates to the result 
    added_once = set()
    
    # Iterate through the list
    for num in my_list:
        # If the number appears more than once
        if my_list.count(num) > 1:
            # Only add the number if it hasn't been added once already
            if num not in added_once:
                duplicates.append(num)
                added_once.add(num)
            
            # Always add duplicate
            duplicates.append(num)
    
    return duplicates