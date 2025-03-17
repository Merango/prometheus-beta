import pytest
from src.temperature_converter import celsius_to_fahrenheit

def test_freezing_point():
    """Test conversion of 0°C to 32°F"""
    assert celsius_to_fahrenheit(0) == 32

def test_boiling_point():
    """Test conversion of 100°C to 212°F"""
    assert celsius_to_fahrenheit(100) == 212

def test_negative_temperature():
    """Test conversion of negative temperature"""
    assert celsius_to_fahrenheit(-40) == -40

def test_decimal_temperature():
    """Test conversion of decimal temperature"""
    assert round(celsius_to_fahrenheit(37.5), 1) == 99.5

def test_invalid_input_type():
    """Test that TypeError is raised for non-numeric input"""
    with pytest.raises(TypeError, match="Input must be a number"):
        celsius_to_fahrenheit("not a number")

def test_none_input():
    """Test that TypeError is raised for None input"""
    with pytest.raises(TypeError, match="Input must be a number"):
        celsius_to_fahrenheit(None)