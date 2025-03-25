import pytest
from src.dot_case import to_dot_case

def test_basic_conversion():
    """Test basic string conversions to dot case."""
    assert to_dot_case("HelloWorld") == "hello.world"
    assert to_dot_case("hello_world") == "hello.world"
    assert to_dot_case("hello-world") == "hello.world"
    assert to_dot_case("Hello World") == "hello.world"

def test_camel_case():
    """Test conversion of camelCase strings."""
    assert to_dot_case("helloWorld") == "hello.world"
    assert to_dot_case("HelloWorld") == "hello.world"
    assert to_dot_case("hello2World") == "hello.2.world"

def test_snake_case():
    """Test conversion of snake_case strings."""
    assert to_dot_case("hello_world_test") == "hello.world.test"
    assert to_dot_case("HELLO_WORLD") == "hello.world"

def test_kebab_case():
    """Test conversion of kebab-case strings."""
    assert to_dot_case("hello-world-test") == "hello.world.test"

def test_mixed_case_and_special_chars():
    """Test conversion with mixed case and special characters."""
    assert to_dot_case("Hello! World") == "hello.world"
    assert to_dot_case("Hello_World-Test") == "hello.world.test"
    assert to_dot_case("hello123World") == "hello.123.world"

def test_edge_cases():
    """Test edge cases of the dot case conversion."""
    assert to_dot_case("") == ""
    assert to_dot_case("a") == "a"
    assert to_dot_case("ABC") == "abc"

def test_error_handling():
    """Test error handling for invalid input types."""
    with pytest.raises(TypeError):
        to_dot_case(123)
    with pytest.raises(TypeError):
        to_dot_case(None)
    with pytest.raises(TypeError):
        to_dot_case(["hello", "world"])

def test_special_characters():
    """Test handling of various special characters."""
    assert to_dot_case("hello@world") == "hello.world"
    assert to_dot_case("hello world!") == "hello.world"
    assert to_dot_case("hello_world!test") == "hello.world.test"