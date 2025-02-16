import pytest
from src.string_converter import convert_to_header_case

def test_convert_to_header_case_basic():
    assert convert_to_header_case("hello world") == "Hello World"
    assert convert_to_header_case("hello_world") == "Hello World"
    assert convert_to_header_case("hello-world") == "Hello World"

def test_convert_to_header_case_multiple_words():
    assert convert_to_header_case("this is a test") == "This Is A Test"
    assert convert_to_header_case("python_string_conversion") == "Python String Conversion"

def test_convert_to_header_case_mixed_delimiters():
    assert convert_to_header_case("hello_world-test") == "Hello World Test"

def test_convert_to_header_case_empty_input():
    assert convert_to_header_case("") == ""

def test_convert_to_header_case_single_word():
    assert convert_to_header_case("hello") == "Hello"

def test_convert_to_header_case_already_header_case():
    assert convert_to_header_case("Hello World") == "Hello World"

def test_convert_to_header_case_invalid_input():
    with pytest.raises(TypeError):
        convert_to_header_case(123)
    with pytest.raises(TypeError):
        convert_to_header_case(None)