import pytest
from src.path_case_converter import convert_to_path_case

def test_basic_conversion():
    """Test basic string conversion to path case."""
    assert convert_to_path_case("hello world") == "hello/world"

def test_multiple_spaces():
    """Test conversion with multiple consecutive spaces."""
    assert convert_to_path_case("hello   world") == "hello/world"

def test_mixed_special_characters():
    """Test conversion with mixed special characters."""
    assert convert_to_path_case("hello, world! test") == "hello/world/test"

def test_mixed_case_input():
    """Test conversion with mixed case input."""
    assert convert_to_path_case("HelloWorld") == "hello/world"

def test_numeric_input():
    """Test conversion with numeric input."""
    assert convert_to_path_case("hello 123 world") == "hello/123/world"

def test_leading_trailing_spaces():
    """Test conversion with leading and trailing spaces."""
    assert convert_to_path_case("  hello world  ") == "hello/world"

def test_all_special_characters():
    """Test conversion with all special characters."""
    assert convert_to_path_case("!@#$%^&*()") == ""

def test_type_error():
    """Test that TypeError is raised for non-string input."""
    with pytest.raises(TypeError, match="Input must be a string"):
        convert_to_path_case(123)

def test_empty_string():
    """Test that ValueError is raised for empty string."""
    with pytest.raises(ValueError, match="Input string cannot be empty"):
        convert_to_path_case("")

def test_empty_after_cleanup():
    """Test string that becomes empty after removing special characters."""
    assert convert_to_path_case("!@#") == ""