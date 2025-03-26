def climb_stairs(n: int) -> int:
    """
    Calculate the number of distinct ways to climb a staircase.
    
    This recursive function determines the number of ways to climb 
    a staircase with n steps, where you can climb either 1 or 2 steps at a time.
    
    Args:
        n (int): Total number of steps in the staircase.
        
    Returns:
        int: Number of distinct ways to climb the staircase.
        
    Raises:
        ValueError: If the number of steps is negative.
    
    Examples:
        >>> climb_stairs(2)
        2
        >>> climb_stairs(3)
        3
    """
    # Handle edge cases
    if n < 0:
        raise ValueError("Number of steps cannot be negative")
    
    # Base cases
    if n <= 1:
        return 1
    
    # Recursive case: number of ways is sum of ways from previous two steps
    return climb_stairs(n - 1) + climb_stairs(n - 2)