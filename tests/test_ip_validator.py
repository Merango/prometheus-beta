import pytest
from src.ip_validator import is_valid_ip_address

def test_valid_ip_addresses():
    valid_ips = [
        "192.168.0.1",
        "10.0.0.0",
        "172.16.0.1",
        "255.255.255.255",
        "0.0.0.0"
    ]
    for ip in valid_ips:
        assert is_valid_ip_address(ip) is True, f"{ip} should be a valid IP address"

def test_invalid_ip_addresses():
    invalid_ips = [
        "256.0.0.1",  # Octet > 255
        "1.2.3.4.5",  # Too many octets
        "1.2.3",      # Too few octets
        "192.168.0",  # Incomplete IP
        "192.168.0.01",  # Leading zero
        "192.168.0.-1",  # Negative number
        "abc.def.ghi.jkl",  # Non-numeric
        "",           # Empty string
        None,         # None
        "   ",        # Whitespace
        "192.168.0.1.",  # Trailing dot
        ".192.168.0.1"   # Leading dot
    ]
    for ip in invalid_ips:
        assert is_valid_ip_address(ip) is False, f"{ip} should be an invalid IP address"

def test_edge_cases():
    # Additional edge case testing
    assert is_valid_ip_address("001.002.003.004") is False  # Leading zeros
    assert is_valid_ip_address("1.2.3.4 ") is False  # Trailing whitespace
    assert is_valid_ip_address(" 1.2.3.4") is False  # Leading whitespace