def solve_knapsack(items, capacity):
    """
    Solve the 0/1 Knapsack Problem using dynamic programming.

    Args:
        items (list): A list of tuples (value, weight) representing items.
        capacity (int): Maximum weight capacity of the knapsack.

    Returns:
        int: Maximum value that can be achieved without exceeding weight capacity.

    Raises:
        ValueError: If inputs are invalid (negative weights/values or non-integer capacity).
    """
    # Input validation
    if not isinstance(capacity, int) or capacity < 0:
        raise ValueError("Capacity must be a non-negative integer")
    
    if not items:
        return 0
    
    # Validate each item
    for value, weight in items:
        if not isinstance(value, (int, float)) or value < 0:
            raise ValueError("Item values must be non-negative numbers")
        if not isinstance(weight, int) or weight < 0:
            raise ValueError("Item weights must be non-negative integers")
    
    # Create dynamic programming table
    n = len(items)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    
    # Build table bottom-up
    for i in range(1, n + 1):
        item_value, item_weight = items[i-1]
        
        for w in range(capacity + 1):
            # Don't include current item
            dp[i][w] = dp[i-1][w]
            
            # Include current item if possible
            if item_weight <= w:
                dp[i][w] = max(dp[i][w], dp[i-1][w - item_weight] + item_value)
    
    # Return maximum value
    return dp[n][capacity]