import pytest
from src.knapsack import solve_knapsack

def test_basic_knapsack():
    """Test a basic knapsack scenario."""
    items = [(60, 10), (100, 20), (120, 30)]
    capacity = 50
    assert solve_knapsack(items, capacity) == 220

def test_empty_items():
    """Test with no items."""
    assert solve_knapsack([], 10) == 0

def test_zero_capacity():
    """Test with zero capacity."""
    items = [(10, 5), (20, 10)]
    assert solve_knapsack(items, 0) == 0

def test_cannot_fit_any_item():
    """Test when no items can fit in the knapsack."""
    items = [(10, 20), (20, 30)]
    assert solve_knapsack(items, 10) == 0

def test_single_item():
    """Test with a single item."""
    items = [(50, 10)]
    assert solve_knapsack(items, 10) == 50
    assert solve_knapsack(items, 5) == 0

def test_multiple_same_value_items():
    """Test with multiple items of similar characteristics."""
    items = [(10, 2), (10, 2), (10, 2)]
    assert solve_knapsack(items, 4) == 20
    assert solve_knapsack(items, 6) == 30

def test_invalid_capacity_negative():
    """Test raising ValueError for negative capacity."""
    with pytest.raises(ValueError, match="Capacity must be a non-negative integer"):
        solve_knapsack([(10, 5)], -1)

def test_invalid_capacity_non_integer():
    """Test raising ValueError for non-integer capacity."""
    with pytest.raises(ValueError, match="Capacity must be a non-negative integer"):
        solve_knapsack([(10, 5)], 3.14)

def test_invalid_item_negative_value():
    """Test raising ValueError for negative item value."""
    with pytest.raises(ValueError, match="Item values must be non-negative numbers"):
        solve_knapsack([(-10, 5)], 10)

def test_invalid_item_negative_weight():
    """Test raising ValueError for negative item weight."""
    with pytest.raises(ValueError, match="Item weights must be non-negative integers"):
        solve_knapsack([(10, -5)], 10)

def test_floating_point_items():
    """Test handling of floating point values."""
    items = [(10.5, 2), (20.3, 3)]
    assert solve_knapsack(items, 5) == 30.8