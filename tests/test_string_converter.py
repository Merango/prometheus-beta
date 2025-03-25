import pytest
from src.string_converter import to_alternating_path_case

def test_space_separated():
    assert to_alternating_path_case("hello world") == "Hello-world"
    assert to_alternating_path_case("python is awesome") == "Python-is-Awesome"

def test_underscore_separated():
    assert to_alternating_path_case("hello_world") == "Hello-world"
    assert to_alternating_path_case("python_is_awesome") == "Python-is-Awesome"

def test_hyphen_separated():
    assert to_alternating_path_case("hello-world") == "Hello-world"
    assert to_alternating_path_case("python-is-awesome") == "Python-is-Awesome"

def test_single_word():
    assert to_alternating_path_case("hello") == "Hello"
    assert to_alternating_path_case("world") == "World"

def test_empty_string():
    assert to_alternating_path_case("") == ""

def test_mixed_separators():
    assert to_alternating_path_case("hello world_test-case") == "Hello-world-Test-case"

def test_error_handling():
    with pytest.raises(TypeError):
        to_alternating_path_case(123)
    with pytest.raises(TypeError):
        to_alternating_path_case(None)

def test_already_capitalized():
    assert to_alternating_path_case("Hello World") == "Hello-world"