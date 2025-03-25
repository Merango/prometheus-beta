import pytest
import math
from src.variance_calculator import calculate_variance

def test_basic_variance():
    """Test variance calculation for a simple list of numbers."""
    numbers = [1, 2, 3, 4, 5]
    expected_variance = 2.5  # (1^2 + 1^2 + 1^2 + 1^2 + 1^2) / 4
    assert math.isclose(calculate_variance(numbers), expected_variance, rel_tol=1e-9)

def test_variance_with_floats():
    """Test variance calculation with floating-point numbers."""
    numbers = [1.5, 2.5, 3.5, 4.5, 5.5]
    expected_variance = 2.5
    assert math.isclose(calculate_variance(numbers), expected_variance, rel_tol=1e-9)

def test_single_element_list():
    """Test variance for a list with a single element."""
    numbers = [42]
    assert calculate_variance(numbers) == 0.0

def test_empty_list_raises_error():
    """Verify that an empty list raises a ValueError."""
    with pytest.raises(ValueError, match="Cannot calculate variance of an empty list"):
        calculate_variance([])

def test_non_list_input_raises_error():
    """Verify that non-list inputs raise a TypeError."""
    with pytest.raises(TypeError, match="Input must be a list"):
        calculate_variance("not a list")

def test_non_numeric_list_raises_error():
    """Verify that lists with non-numeric elements raise a TypeError."""
    with pytest.raises(TypeError, match="All elements must be numeric"):
        calculate_variance([1, 2, "three", 4, 5])

def test_large_numbers():
    """Test variance calculation with large numbers."""
    numbers = [10000, 20000, 30000, 40000, 50000]
    expected_variance = 2.5e9  # Rough calculation
    assert math.isclose(calculate_variance(numbers), expected_variance, rel_tol=1e-9)

def test_negative_numbers():
    """Test variance calculation with negative numbers."""
    numbers = [-1, -2, -3, -4, -5]
    expected_variance = 2.5
    assert math.isclose(calculate_variance(numbers), expected_variance, rel_tol=1e-9)

def test_mixed_numbers():
    """Test variance calculation with mixed positive and negative numbers."""
    numbers = [-10, 0, 10, 20, 30]
    expected_variance = 200.0
    assert math.isclose(calculate_variance(numbers), expected_variance, rel_tol=1e-9)