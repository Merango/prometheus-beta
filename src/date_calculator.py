from datetime import datetime

def calculate_days_between_dates(date1, date2):
    """
    Calculate the number of days between two dates.

    Args:
        date1 (str or datetime): First date in ISO format (YYYY-MM-DD) or datetime object
        date2 (str or datetime): Second date in ISO format (YYYY-MM-DD) or datetime object

    Returns:
        int: Absolute number of days between the two dates

    Raises:
        ValueError: If dates are invalid or cannot be parsed
        TypeError: If input is not a string or datetime object
    """
    # Convert inputs to datetime objects if they are strings
    if isinstance(date1, str):
        try:
            date1 = datetime.fromisoformat(date1).date()
        except ValueError:
            raise ValueError(f"Invalid date format for date1: {date1}")
    
    if isinstance(date2, str):
        try:
            date2 = datetime.fromisoformat(date2).date()
        except ValueError:
            raise ValueError(f"Invalid date format for date2: {date2}")
    
    # Validate input types
    if not hasattr(date1, 'date') or not hasattr(date2, 'date'):
        raise TypeError("Inputs must be datetime or date objects, or ISO format date strings")
    
    # Calculate absolute difference in days
    return abs((date2 - date1).days)