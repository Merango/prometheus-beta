import pytest
from datetime import date
import sys
import os

# Add the project root directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.date_utils import get_current_date

def test_get_current_date():
    # Get the current date using datetime
    expected_date = date.today().strftime("%Y-%m-%d")
    
    # Call the function
    result = get_current_date()
    
    # Check if the result matches the expected date format
    assert result == expected_date, f"Expected {expected_date}, but got {result}"
    
    # Check date format
    assert len(result) == 10, "Date should be in YYYY-MM-DD format (10 characters)"
    assert result[4] == '-', "Fourth character should be a hyphen"
    assert result[7] == '-', "Seventh character should be a hyphen"
    
    # Validate that all other characters are digits
    assert result.replace('-', '').isdigit(), "Date should only contain digits except for hyphens"