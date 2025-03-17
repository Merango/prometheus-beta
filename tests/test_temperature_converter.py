import pytest
from src.temperature_converter import fahrenheit_to_celsius

def test_known_conversions():
    """Test known Fahrenheit to Celsius conversions."""
    assert fahrenheit_to_celsius(32) == 0  # Freezing point of water
    assert fahrenheit_to_celsius(212) == 100  # Boiling point of water
    assert fahrenheit_to_celsius(98.6) == 37  # Normal body temperature

def test_negative_temperatures():
    """Test conversion of negative temperatures."""
    assert fahrenheit_to_celsius(-40) == -40  # Unique point where F and C are equal
    assert fahrenheit_to_celsius(-22) == -30

def test_decimal_temperatures():
    """Test conversion of decimal temperatures."""
    assert fahrenheit_to_celsius(50.5) == 10.28

def test_large_temperatures():
    """Test conversion of large temperatures."""
    assert fahrenheit_to_celsius(1000) == 537.78

def test_error_handling():
    """Test error handling for invalid inputs."""
    # Test non-numeric inputs
    with pytest.raises(TypeError):
        fahrenheit_to_celsius("not a number")
    
    with pytest.raises(TypeError):
        fahrenheit_to_celsius(None)
    
    with pytest.raises(TypeError):
        fahrenheit_to_celsius([32])