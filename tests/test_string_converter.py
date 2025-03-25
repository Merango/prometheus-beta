import pytest
from src.string_converter import convert_to_alternating_pascal_case

def test_basic_conversion():
    """Test basic string conversion to alternating Pascal case."""
    assert convert_to_alternating_pascal_case("hello world") == "HeLlOWoRlD"
    assert convert_to_alternating_pascal_case("python is awesome") == "PyThOnIsAwEsOmE"

def test_single_word():
    """Test conversion of a single word."""
    assert convert_to_alternating_pascal_case("python") == "PyThOn"

def test_multiple_words():
    """Test conversion of multiple words."""
    assert convert_to_alternating_pascal_case("one two three") == "OneTwOThReE"

def test_mixed_case_input():
    """Test input with mixed case."""
    assert convert_to_alternating_pascal_case("HeLLo WoRLd") == "HeLlOWoRlD"

def test_input_with_extra_whitespace():
    """Test input with extra whitespace."""
    assert convert_to_alternating_pascal_case("  hello   world  ") == "HeLlOWoRlD"

def test_error_handling():
    """Test error handling for invalid inputs."""
    # Test non-string input
    with pytest.raises(TypeError, match="Input must be a string"):
        convert_to_alternating_pascal_case(123)
    
    # Test empty string
    with pytest.raises(ValueError, match="Input string cannot be empty"):
        convert_to_alternating_pascal_case("")

def test_special_characters():
    """Test conversion with special characters."""
    assert convert_to_alternating_pascal_case("hello, world!") == "HeLlOWoRlD"