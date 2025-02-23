import pytest
from src.parity_subsequence import longest_parity_subsequence

def test_mixed_array_with_even_subsequence():
    # Mixed array with longer even subsequence
    arr = [1, 2, 3, 4, 6, 8, 5, 7]
    assert longest_parity_subsequence(arr) == [4, 6, 8]

def test_mixed_array_with_odd_subsequence():
    # Mixed array with longer odd subsequence
    arr = [2, 4, 1, 3, 5, 6, 7]
    assert longest_parity_subsequence(arr) == [1, 3, 5]

def test_all_even_array():
    # All even array
    arr = [2, 4, 6, 8, 10]
    assert longest_parity_subsequence(arr) == [2, 4, 6, 8, 10]

def test_all_odd_array():
    # All odd array
    arr = [1, 3, 5, 7, 9]
    assert longest_parity_subsequence(arr) == [1, 3, 5, 7, 9]

def test_single_element_arrays():
    # Single even element
    assert longest_parity_subsequence([2]) == [2]
    # Single odd element
    assert longest_parity_subsequence([1]) == [1]

def test_empty_array_raises_error():
    with pytest.raises(ValueError, match="Input list cannot be empty"):
        longest_parity_subsequence([])

def test_non_list_input_raises_error():
    with pytest.raises(TypeError, match="Input must be a list of integers"):
        longest_parity_subsequence("not a list")
        longest_parity_subsequence(123)

def test_complex_mixed_parity():
    # Complex scenario with multiple subsequences
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5]
    assert longest_parity_subsequence(arr) == [2, 3, 4, 5]

def test_alternating_parity():
    # Alternating parity
    arr = [1, 2, 3, 4, 5, 6]
    result = longest_parity_subsequence(arr)
    assert (result == [1, 3, 5] or result == [2, 4, 6])

def test_edge_cases():
    # Minimal sequences
    assert longest_parity_subsequence([2, 1]) == [2]
    assert longest_parity_subsequence([1, 2]) == [1]