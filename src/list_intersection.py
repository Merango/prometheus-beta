def find_list_intersection(list1, list2):
    """
    Find the intersection of two lists.
    
    Args:
        list1 (list): First input list
        list2 (list): Second input list
    
    Returns:
        list: A list containing common elements between list1 and list2
    """
    # Use set intersection to find common elements efficiently
    # Convert back to list to maintain function signature
    return list(set(list1) & set(list2))