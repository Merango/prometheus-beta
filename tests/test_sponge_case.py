import pytest
from src.sponge_case import convert_to_sponge_case

def test_convert_to_sponge_case_basic():
    """Test basic sponge case conversion"""
    assert convert_to_sponge_case("hello") == "hElLo"
    assert convert_to_sponge_case("world") == "wOrLd"

def test_convert_to_sponge_case_mixed_case():
    """Test sponge case conversion with mixed input"""
    assert convert_to_sponge_case("PyThOn") == "pYtHoN"

def test_convert_to_sponge_case_empty_string():
    """Test sponge case conversion with empty string"""
    assert convert_to_sponge_case("") == ""

def test_convert_to_sponge_case_spaces():
    """Test sponge case conversion with spaces"""
    assert convert_to_sponge_case("hello world") == "hElLo WoRlD"

def test_convert_to_sponge_case_special_chars():
    """Test sponge case conversion with special characters"""
    assert convert_to_sponge_case("hello123!@#") == "hElLo123!@#"

def test_convert_to_sponge_case_invalid_input():
    """Test that TypeError is raised for non-string inputs"""
    with pytest.raises(TypeError):
        convert_to_sponge_case(123)
    with pytest.raises(TypeError):
        convert_to_sponge_case(None)