import pytest
from src.alternating_camel_case import to_alternating_camel_case

def test_basic_conversion():
    """Test basic string conversion"""
    assert to_alternating_camel_case("hello world") == "HeLlO WoRlD"
    assert to_alternating_camel_case("python programming") == "PyThOn PrOgRaMmInG"

def test_single_word():
    """Test conversion of a single word"""
    assert to_alternating_camel_case("python") == "PyThOn"

def test_empty_string():
    """Test that empty string raises ValueError"""
    with pytest.raises(ValueError, match="Input string cannot be empty"):
        to_alternating_camel_case("")

def test_non_string_input():
    """Test that non-string input raises TypeError"""
    with pytest.raises(TypeError, match="Input must be a string"):
        to_alternating_camel_case(123)
        to_alternating_camel_case(None)

def test_special_characters():
    """Test conversion with special characters and spaces"""
    assert to_alternating_camel_case("hello, world!") == "HeLlO, WoRlD!"
    assert to_alternating_camel_case("  spaces  ") == "  SpAcEs  "

def test_already_mixed_case():
    """Test conversion of strings with mixed case"""
    assert to_alternating_camel_case("AlReAdY MiXeD") == "AlReAdY MiXeD"