"""
Test suite for LZC Compression Algorithm Implementation.
"""

import pytest
from src.lzc_compression import lzc_compress, lzc_decompress

def test_basic_compression_decompression():
    """Test basic string compression and decompression."""
    original = "HELLO WORLD"
    compressed = lzc_compress(original)
    decompressed = lzc_decompress(compressed).decode('utf-8')
    assert decompressed == original

def test_repeated_characters():
    """Test compression of repeated characters."""
    original = "AAAAAAAA"
    compressed = lzc_compress(original)
    decompressed = lzc_decompress(compressed).decode('utf-8')
    assert decompressed == original

def test_mixed_bytes():
    """Test compression of mixed byte sequences."""
    original = b'\x00\x01\x02\x00\x01\x02\x03'
    compressed = lzc_compress(original)
    decompressed = lzc_decompress(compressed)
    assert decompressed == original

def test_long_input():
    """Test compression of a longer input."""
    original = "This is a longer test string with some repeated patterns to compress"
    compressed = lzc_compress(original)
    decompressed = lzc_decompress(compressed).decode('utf-8')
    assert decompressed == original

def test_binary_data():
    """Test compression of binary data."""
    original = bytes([0, 1, 2, 3, 4, 5, 0, 1, 2, 3, 4, 5, 6])
    compressed = lzc_compress(original)
    decompressed = lzc_decompress(compressed)
    assert decompressed == original

def test_empty_input_raises_error():
    """Test that empty input raises a ValueError."""
    with pytest.raises(ValueError):
        lzc_compress(b'')
    with pytest.raises(ValueError):
        lzc_decompress([])

def test_invalid_input_types():
    """Test that invalid input types raise TypeError."""
    with pytest.raises(TypeError):
        lzc_compress(123)
    with pytest.raises(TypeError):
        lzc_decompress('not a list')
    with pytest.raises(TypeError):
        lzc_decompress([1, 2, 'invalid'])

def test_invalid_compression_code():
    """Test that invalid compression codes raise ValueError."""
    with pytest.raises(ValueError):
        lzc_decompress([1000000])  # Unreasonably large code

def test_roundtrip_consistency():
    """Test multiple roundtrip compressions to ensure consistency."""
    test_cases = [
        "Hello, world!",
        "Repeated repeated repeated words",
        "12345678901234567890",
        b'\x00\x01\x02\x03\x04\x05'
    ]
    
    for original in test_cases:
        # If it's a string, convert to bytes for consistent testing
        input_data = original.encode('utf-8') if isinstance(original, str) else original
        
        # Compress
        compressed = lzc_compress(input_data)
        
        # Decompress
        decompressed = lzc_decompress(compressed)
        
        # Assert equality
        assert decompressed == input_data, f"Failed for input: {original}"