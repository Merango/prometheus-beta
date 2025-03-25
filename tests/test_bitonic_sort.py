import pytest
from src.bitonic_sort import bitonic_sort

def test_bitonic_sort_ascending():
    """Test bitonic sort in ascending order"""
    input_list = [64, 34, 25, 12, 22, 11, 90]
    expected = sorted(input_list)
    assert bitonic_sort(input_list) == expected

def test_bitonic_sort_descending():
    """Test bitonic sort in descending order"""
    input_list = [64, 34, 25, 12, 22, 11, 90]
    expected = sorted(input_list, reverse=True)
    assert bitonic_sort(input_list, ascending=False) == expected

def test_bitonic_sort_empty_list():
    """Test sorting an empty list"""
    assert bitonic_sort([]) == []

def test_bitonic_sort_single_element():
    """Test sorting a list with a single element"""
    single_element_list = [42]
    assert bitonic_sort(single_element_list) == [42]

def test_bitonic_sort_already_sorted():
    """Test sorting an already sorted list"""
    sorted_list = [1, 2, 3, 4, 5]
    assert bitonic_sort(sorted_list) == sorted_list

def test_bitonic_sort_reverse_sorted():
    """Test sorting a reverse sorted list"""
    reverse_sorted = [5, 4, 3, 2, 1]
    assert bitonic_sort(reverse_sorted) == [1, 2, 3, 4, 5]

def test_bitonic_sort_with_duplicates():
    """Test sorting a list with duplicate elements"""
    list_with_duplicates = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    expected = sorted(list_with_duplicates)
    assert bitonic_sort(list_with_duplicates) == expected

def test_bitonic_sort_invalid_input_type():
    """Test that a TypeError is raised for invalid input type"""
    with pytest.raises(TypeError):
        bitonic_sort("not a list")

def test_bitonic_sort_with_mixed_types():
    """Test sorting a list with mixed numeric types"""
    mixed_list = [3, 1.5, 4, 2.7, 5]
    expected = sorted(mixed_list)
    assert bitonic_sort(mixed_list) == expected

def test_bitonic_sort_large_list():
    """Test sorting a larger list"""
    import random
    large_list = [random.randint(1, 1000) for _ in range(100)]
    expected = sorted(large_list)
    assert bitonic_sort(large_list) == expected