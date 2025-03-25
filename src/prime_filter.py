def filter_primes(numbers):
    """
    Filter out prime numbers from a given list of numbers.
    
    Args:
        numbers (list): A list of integers (positive and negative)
    
    Returns:
        list: A list of prime numbers from the input list
    
    Notes:
        - 0 and 1 are not considered prime numbers
        - Negative numbers are checked for primality by their absolute value
    """
    def is_prime(n):
        # Handle special cases
        if n < 2:
            return False
        
        # Check for primality using absolute value
        n = abs(n)
        
        # Optimize primality check
        if n == 2:
            return True
        
        # Even numbers > 2 are not prime
        if n % 2 == 0:
            return False
        
        # Check odd divisors up to square root of n
        for i in range(3, int(n**0.5) + 1, 2):
            if n % i == 0:
                return False
        
        return True
    
    # Return list of prime numbers
    return [num for num in numbers if is_prime(num)]