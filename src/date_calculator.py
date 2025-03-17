from datetime import datetime, date

def calculate_days_between_dates(date1, date2):
    """
    Calculate the number of days between two dates.

    Args:
        date1 (str or datetime or date): First date in ISO format (YYYY-MM-DD) or datetime/date object
        date2 (str or datetime or date): Second date in ISO format (YYYY-MM-DD) or datetime/date object

    Returns:
        int: Absolute number of days between the two dates

    Raises:
        ValueError: If dates are invalid or cannot be parsed
        TypeError: If input is not a string, datetime, or date object
    """
    # Convert inputs to date objects if they are strings
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
    
    # Convert datetime objects to date objects if needed
    if isinstance(date1, datetime):
        date1 = date1.date()
    
    if isinstance(date2, datetime):
        date2 = date2.date()
    
    # Validate input types
    if not isinstance(date1, date) or not isinstance(date2, date):
        raise TypeError("Inputs must be datetime, date objects, or ISO format date strings")
    
    # Calculate absolute difference in days
    return abs((date2 - date1).days)