"""
Unit tests for LZJH compression algorithm.
"""

import pytest
import random
import string

from src.lzjh_compression import lzjh_compress, lzjh_decompress

def test_basic_compression_decompression():
    """Test basic compression and decompression"""
    original = b"HELLO WORLD"
    compressed = lzjh_compress(original)
    decompressed = lzjh_decompress(compressed)
    assert decompressed == original

def test_repeated_patterns():
    """Test compression of repeated patterns"""
    original = b"AAAAAAAAAABBBBBBBBBB"
    compressed = lzjh_compress(original)
    decompressed = lzjh_decompress(compressed)
    assert decompressed == original

def test_string_input():
    """Test string input compression"""
    original = "Hello, world! This is a test of LZJH compression."
    compressed = lzjh_compress(original)
    decompressed = lzjh_decompress(compressed)
    assert decompressed.decode('utf-8') == original

def test_random_data():
    """Test compression with random data"""
    # Generate random bytes
    original = bytes(random.getrandbits(8) for _ in range(1000))
    compressed = lzjh_compress(original)
    decompressed = lzjh_decompress(compressed)
    assert decompressed == original

def test_empty_input_error():
    """Test error handling for empty input"""
    with pytest.raises(ValueError, match="Input data cannot be empty"):
        lzjh_compress(b"")
    
    with pytest.raises(ValueError, match="Compressed data cannot be empty"):
        lzjh_decompress(b"")

def test_invalid_input_type():
    """Test error handling for invalid input types"""
    with pytest.raises(TypeError, match="Input must be bytes or str"):
        lzjh_compress(123)
    
    with pytest.raises(TypeError, match="Compressed data must be bytes"):
        lzjh_decompress(123)

def test_large_input():
    """Test compression with larger input"""
    # Generate a larger string with some repetition
    original = ''.join(random.choices(string.ascii_letters + string.digits, k=10000))
    compressed = lzjh_compress(original)
    decompressed = lzjh_decompress(compressed)
    assert decompressed.decode('utf-8') == original