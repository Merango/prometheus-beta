import pytest
from src.matrix_reversal import reverse_matrix_elements

def test_basic_matrix_reversal():
    """Test basic matrix element reversal"""
    input_matrix = [
        [1, 23, 45],
        [67, 8, 90],
        [12, 34, 56]
    ]
    expected_matrix = [
        [1, 32, 54],
        [76, 8, 9],
        [21, 43, 65]
    ]
    assert reverse_matrix_elements(input_matrix) == expected_matrix

def test_single_digit_matrix():
    """Test matrix with single-digit elements"""
    input_matrix = [
        [1, 2],
        [3, 4]
    ]
    expected_matrix = [
        [1, 2],
        [3, 4]
    ]
    assert reverse_matrix_elements(input_matrix) == expected_matrix

def test_zero_elements():
    """Test matrix with zero elements"""
    input_matrix = [
        [0, 0],
        [0, 0]
    ]
    expected_matrix = [
        [0, 0],
        [0, 0]
    ]
    assert reverse_matrix_elements(input_matrix) == expected_matrix

def test_invalid_matrix_non_square():
    """Test non-square matrix raises ValueError"""
    invalid_matrix = [
        [1, 2, 3],
        [4, 5]
    ]
    with pytest.raises(ValueError, match="Matrix must be square"):
        reverse_matrix_elements(invalid_matrix)

def test_invalid_matrix_out_of_range():
    """Test matrix with large elements"""
    invalid_matrix = [
        [1, 2],
        [1000, 3]
    ]
    with pytest.raises(ValueError, match="Matrix elements must be integers within"):
        reverse_matrix_elements(invalid_matrix)

def test_matrix_size_validation():
    """Test matrix size validation"""
    # Empty matrix
    with pytest.raises(ValueError, match="Matrix cannot be empty"):
        reverse_matrix_elements([])
    
    # Oversized matrix (would raise ValueError due to size)
    large_matrix = [[i for i in range(1001)] for _ in range(1001)]
    with pytest.raises(ValueError, match="Matrix size must be between 1 and 1000"):
        reverse_matrix_elements(large_matrix)

def test_matrix_with_mixed_length_elements():
    """Test matrix reversal with mixed-length elements"""
    input_matrix = [
        [1, 10, 100],
        [5, 50, 505],
        [7, 70, 707]
    ]
    expected_matrix = [
        [1, 1, 1],
        [5, 5, 505],
        [7, 7, 707]
    ]
    assert reverse_matrix_elements(input_matrix) == expected_matrix