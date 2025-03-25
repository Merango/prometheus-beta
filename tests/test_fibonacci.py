import pytest
from src.fibonacci import fibonacci_generator

def test_fibonacci_zero_numbers():
    assert fibonacci_generator(0) == []

def test_fibonacci_one_number():
    assert fibonacci_generator(1) == [0]

def test_fibonacci_two_numbers():
    assert fibonacci_generator(2) == [0, 1]

def test_fibonacci_multiple_numbers():
    assert fibonacci_generator(5) == [0, 1, 1, 2, 3]
    assert fibonacci_generator(7) == [0, 1, 1, 2, 3, 5, 8]

def test_fibonacci_negative_input():
    with pytest.raises(ValueError, match="Number of Fibonacci numbers must be non-negative"):
        fibonacci_generator(-1)

def test_fibonacci_invalid_input_type():
    with pytest.raises(TypeError, match="Input must be an integer"):
        fibonacci_generator("5")
    with pytest.raises(TypeError, match="Input must be an integer"):
        fibonacci_generator(5.5)
    with pytest.raises(TypeError, match="Input must be an integer"):
        fibonacci_generator(None)