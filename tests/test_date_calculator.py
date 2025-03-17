import pytest
from datetime import datetime, date
from src.date_calculator import calculate_days_between_dates

def test_calculate_days_between_dates_same_date():
    """Test calculating days between the same date returns 0"""
    assert calculate_days_between_dates('2023-01-01', '2023-01-01') == 0
    assert calculate_days_between_dates(date(2023, 1, 1), date(2023, 1, 1)) == 0

def test_calculate_days_between_dates_different_dates():
    """Test calculating days between different dates"""
    assert calculate_days_between_dates('2023-01-01', '2023-01-10') == 9
    assert calculate_days_between_dates(date(2023, 1, 1), date(2023, 1, 10)) == 9

def test_calculate_days_between_dates_reversed_order():
    """Test order of dates doesn't matter"""
    assert calculate_days_between_dates('2023-01-10', '2023-01-01') == 9
    assert calculate_days_between_dates(date(2023, 1, 10), date(2023, 1, 1)) == 9

def test_calculate_days_between_dates_datetime_objects():
    """Test with datetime objects"""
    date1 = datetime(2023, 1, 1, 12, 0, 0)
    date2 = datetime(2023, 1, 10, 14, 30, 0)
    assert calculate_days_between_dates(date1, date2) == 9

def test_calculate_days_between_dates_invalid_input():
    """Test error handling for invalid inputs"""
    with pytest.raises(ValueError, match="Invalid date format"):
        calculate_days_between_dates('invalid-date', '2023-01-01')
    
    with pytest.raises(TypeError):
        calculate_days_between_dates(123, '2023-01-01')

def test_calculate_days_between_dates_different_years():
    """Test calculating days between dates in different years"""
    assert calculate_days_between_dates('2022-12-31', '2023-01-01') == 1
    assert calculate_days_between_dates('2020-02-28', '2020-03-01') == 2  # leap year