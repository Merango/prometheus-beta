import pytest
from src.sum_even_indexed_integers import sum_even_indexed_integers

def test_sum_even_indexed_integers():
    # Test with normal list of positive integers
    assert sum_even_indexed_integers([1, 10, 2, 20, 3, 30]) == 6

    # Test with list containing negative integers
    assert sum_even_indexed_integers([-1, 10, -2, 20, -3, 30]) == -6

    # Test with empty list
    assert sum_even_indexed_integers([]) == 0

    # Test with single element list
    assert sum_even_indexed_integers([42]) == 42

    # Test with list of all zeros
    assert sum_even_indexed_integers([0, 10, 0, 20, 0, 30]) == 0

    # Test with list of mixed positive and negative integers
    assert sum_even_indexed_integers([5, -3, 10, -7, 15, -20]) == 30