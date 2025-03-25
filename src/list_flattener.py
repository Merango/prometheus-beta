from typing import List, Union, Any

def flatten_nested_list(nested_list: List[Union[Any, List]]) -> List[Any]:
    """
    Flatten a nested list of arbitrary depth into a single-level list.

    This function recursively traverses through a nested list and returns 
    a flattened version where all nested lists are converted to a single 
    flat list while preserving the order of elements.

    Args:
        nested_list (List[Union[Any, List]]): A potentially nested list 
        containing elements and/or nested lists of any type.

    Returns:
        List[Any]: A flattened list containing all elements from the 
        original nested list.

    Examples:
        >>> flatten_nested_list([1, [2, 3], [4, [5, 6]]])
        [1, 2, 3, 4, 5, 6]
        >>> flatten_nested_list([[1, 2], 3, [4, [5]]])
        [1, 2, 3, 4, 5]
        >>> flatten_nested_list([])
        []
    """
    flattened = []
    
    for item in nested_list:
        # If the item is a list, recursively flatten it
        if isinstance(item, list):
            flattened.extend(flatten_nested_list(item))
        # If the item is not a list, add it directly
        else:
            flattened.append(item)
    
    return flattened