import pytest
from src.run_length_encoding import run_length_encode, run_length_decode

def test_run_length_encode_string():
    # Test basic string encoding
    assert run_length_encode("AABBBCCCC") == [
        ('A', 2), ('B', 3), ('C', 4)
    ]

def test_run_length_encode_list():
    # Test list encoding
    assert run_length_encode([1, 1, 2, 2, 2, 3]) == [
        (1, 2), (2, 3), (3, 1)
    ]

def test_run_length_decode_standard():
    # Test basic decoding
    encoded = [('A', 2), ('B', 3), ('C', 4)]
    assert run_length_decode(encoded) == list("AABBBCCCC")

def test_run_length_encode_single_character():
    # Test single character input
    assert run_length_encode("A") == [('A', 1)]
    assert run_length_encode([1]) == [(1, 1)]

def test_run_length_decode_single_item():
    # Test decoding single item
    assert run_length_decode([('X', 3)]) == ['X', 'X', 'X']

def test_run_length_encode_error_handling():
    # Test invalid input types
    with pytest.raises(TypeError):
        run_length_encode(123)
    
    with pytest.raises(ValueError):
        run_length_encode("")
    
    with pytest.raises(ValueError):
        run_length_encode([])

def test_run_length_decode_error_handling():
    # Test invalid input types for decoding
    with pytest.raises(TypeError):
        run_length_decode("not a list")
    
    with pytest.raises(ValueError):
        run_length_decode([])
    
    with pytest.raises(ValueError):
        run_length_decode([('A', 0)])
    
    with pytest.raises(ValueError):
        run_length_decode([('A', -1)])

def test_roundtrip_encoding_decoding():
    # Test full roundtrip encoding and decoding
    original = list("WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWB")
    encoded = run_length_encode(original)
    decoded = run_length_decode(encoded)
    assert decoded == original