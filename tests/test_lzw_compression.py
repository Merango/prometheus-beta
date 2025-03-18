"""
Tests for LZW Compression and Decompression

This module contains unit tests for the Lempel-Ziv-Welch compression algorithm.
"""

import pytest
from src.lzw_compression import lzw_compress, lzw_decompress

def test_basic_compression_decompression():
    """Test basic string compression and decompression."""
    original = "TOBEORNOTTOBEORTOBEORNOT"
    compressed = lzw_compress(original)
    decompressed = lzw_decompress(compressed)
    assert decompressed == original

def test_single_char_string():
    """Test compression and decompression of a single character string."""
    original = "A"
    compressed = lzw_compress(original)
    decompressed = lzw_decompress(compressed)
    assert decompressed == original

def test_repeated_chars():
    """Test compression and decompression of repeated characters."""
    original = "AAAAAAAAAA"
    compressed = lzw_compress(original)
    decompressed = lzw_decompress(compressed)
    assert decompressed == original

def test_mixed_case_string():
    """Test compression and decompression of mixed case string."""
    original = "HelloWorldHelloWorld"
    compressed = lzw_compress(original)
    decompressed = lzw_decompress(compressed)
    assert decompressed == original

def test_numeric_string():
    """Test compression and decompression of numeric string."""
    original = "12345678901234567890"
    compressed = lzw_compress(original)
    decompressed = lzw_decompress(compressed)
    assert decompressed == original

def test_special_chars_string():
    """Test compression and decompression of string with special characters."""
    original = "Hello, World! @#$%^&*()"
    compressed = lzw_compress(original)
    decompressed = lzw_decompress(compressed)
    assert decompressed == original

def test_invalid_input_types():
    """Test error handling for invalid input types."""
    with pytest.raises(TypeError):
        lzw_compress(12345)
    
    with pytest.raises(TypeError):
        lzw_decompress("not a list")

def test_empty_input():
    """Test error handling for empty inputs."""
    with pytest.raises(ValueError):
        lzw_compress("")
    
    with pytest.raises(ValueError):
        lzw_decompress([])

def test_compression_efficiency():
    """Verify that compression reduces string length."""
    original = "TOBEORNOTTOBEORTOBEORNOT"
    compressed = lzw_compress(original)
    assert len(compressed) < len(original)  # Compressed list is shorter