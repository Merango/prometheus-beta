def symmetric_difference(list1, list2):
    """
    Find the symmetric difference between two lists.
    
    The symmetric difference is a list of elements which are in either of the lists,
    but not in their intersection. Duplicates are preserved.
    
    Args:
        list1 (list): First input list
        list2 (list): Second input list
    
    Returns:
        list: A list containing elements that are in either list1 or list2, but not both
    
    Raises:
        TypeError: If input is not a list
    """
    # Validate input types
    if not isinstance(list1, list) or not isinstance(list2, list):
        raise TypeError("Inputs must be lists")
    
    # Find symmetric difference by manually filtering
    diff = []
    
    # Add elements from list1 not in list2
    for item in list1:
        if item not in list2 or (list2.count(item) < list1.count(item)):
            diff.append(item)
    
    # Add elements from list2 not in list1
    for item in list2:
        if item not in list1 or (list1.count(item) < list2.count(item)):
            diff.append(item)
    
    return diff