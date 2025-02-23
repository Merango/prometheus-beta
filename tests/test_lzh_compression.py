"""
Unit tests for LZH compression module.
"""

import pytest
import sys
import os

# Ensure the src directory is in the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from lzh_compression import lzh_compress, lzh_decompress

def test_basic_compression_decompression():
    """Test basic compression and decompression of a simple string."""
    original = "hello world"
    compressed = lzh_compress(original)
    decompressed = lzh_decompress(compressed)
    assert decompressed.decode('utf-8') == original

def test_byte_compression_decompression():
    """Test compression and decompression of byte data."""
    original = b'\x00\x01\x02\x03\x04'
    compressed = lzh_compress(original)
    decompressed = lzh_decompress(compressed)
    assert decompressed == original

def test_repeated_patterns():
    """Test compression of data with repeated patterns."""
    original = "aaaaaabbbbbbcccccc"
    compressed = lzh_compress(original)
    decompressed = lzh_decompress(compressed)
    assert decompressed.decode('utf-8') == original

def test_empty_input_raises_error():
    """Test that empty input raises a ValueError."""
    with pytest.raises(ValueError):
        lzh_compress("")
    with pytest.raises(ValueError):
        lzh_decompress(b'')

def test_invalid_input_type():
    """Test that invalid input types raise a TypeError."""
    with pytest.raises(TypeError):
        lzh_compress(123)
    with pytest.raises(TypeError):
        lzh_decompress(123)

def test_complex_data():
    """Test compression of more complex data."""
    original = "The quick brown fox jumps over the lazy dog" * 5
    compressed = lzh_compress(original)
    decompressed = lzh_decompress(compressed)
    assert decompressed.decode('utf-8') == original

def test_binary_data():
    """Test compression of binary data."""
    original = bytes(range(256)) * 3
    compressed = lzh_compress(original)
    decompressed = lzh_decompress(compressed)
    assert decompressed == original

def test_large_input():
    """Test compression of a large input."""
    original = "lorem ipsum " * 10000
    compressed = lzh_compress(original)
    decompressed = lzh_decompress(compressed)
    assert decompressed.decode('utf-8') == original

def test_symmetric_property():
    """Verify that compress-decompress cycle works symmetrically."""
    test_cases = [
        "hello world",
        "repeated " * 10,
        "mixed 123 symbols @#$%",
        bytes(range(100))
    ]
    
    for original in test_cases:
        if isinstance(original, str):
            original_bytes = original.encode('utf-8')
        else:
            original_bytes = original
        
        compressed = lzh_compress(original_bytes)
        decompressed = lzh_decompress(compressed)
        
        assert decompressed == original_bytes, f"Failed for input: {original}"