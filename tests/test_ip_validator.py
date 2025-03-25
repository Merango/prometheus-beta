import pytest
from src.ip_validator import validate_ipv4_address

def test_valid_ip_addresses():
    """Test valid single-digit IP addresses"""
    assert validate_ipv4_address('1.2.3.4') == True
    assert validate_ipv4_address('0.0.0.0') == True
    assert validate_ipv4_address('9.9.9.9') == True

def test_invalid_ip_addresses():
    """Test invalid IP address formats"""
    # Too many/few octets
    assert validate_ipv4_address('1.2.3') == False
    assert validate_ipv4_address('1.2.3.4.5') == False
    
    # Non-digit characters
    assert validate_ipv4_address('a.b.c.d') == False
    assert validate_ipv4_address('1.2.3.x') == False
    
    # Multi-digit octets
    assert validate_ipv4_address('10.2.3.4') == False
    assert validate_ipv4_address('1.22.3.4') == False
    
    # Out of range digits
    assert validate_ipv4_address('-1.2.3.4') == False
    assert validate_ipv4_address('1.2.3.10') == False

def test_edge_cases():
    """Test edge cases and type handling"""
    # Empty string
    assert validate_ipv4_address('') == False
    
    # Non-string input
    assert validate_ipv4_address(None) == False
    assert validate_ipv4_address(123) == False
    
    # Whitespace
    assert validate_ipv4_address(' 1.2.3.4 ') == False
    assert validate_ipv4_address('1. 2.3.4') == False

def test_dots():
    """Test dot-related edge cases"""
    # Consecutive dots
    assert validate_ipv4_address('1..2.3') == False
    
    # Leading/trailing dots
    assert validate_ipv4_address('.1.2.3.4') == False
    assert validate_ipv4_address('1.2.3.4.') == False