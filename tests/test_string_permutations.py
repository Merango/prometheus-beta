import pytest
from src.string_permutations import generate_unique_permutations

def test_basic_permutations():
    """Test basic string permutations"""
    result = generate_unique_permutations('abc')
    assert set(result) == {'abc', 'acb', 'bac', 'bca', 'cab', 'cba'}
    assert len(result) == 6

def test_string_with_duplicates():
    """Test permutations of a string with duplicate characters"""
    result = generate_unique_permutations('aba')
    assert set(result) == {'aba', 'aab', 'baa'}
    assert len(result) == 3

def test_single_character():
    """Test permutations of a single character"""
    result = generate_unique_permutations('a')
    assert result == ['a']

def test_empty_string():
    """Test permutations of an empty string"""
    result = generate_unique_permutations('')
    assert result == []

def test_invalid_input():
    """Test error handling for non-string input"""
    with pytest.raises(TypeError, match="Input must be a string"):
        generate_unique_permutations(123)
    with pytest.raises(TypeError, match="Input must be a string"):
        generate_unique_permutations(None)

def test_longer_string():
    """Test permutations of a longer string"""
    result = generate_unique_permutations('abcd')
    assert len(result) == 24  # 4! = 24 unique permutations

def test_sorting_consistency():
    """Verify that the output is sorted"""
    result = generate_unique_permutations('cab')
    assert result == ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']