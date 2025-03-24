import re
import pytest
from src.uuid_generator import generate_uuid

def test_uuid_generation():
    """Test basic UUID generation functionality."""
    uuid_str = generate_uuid()
    
    # Check UUID is a string
    assert isinstance(uuid_str, str), "Generated UUID should be a string"
    
    # Check UUID length
    assert len(uuid_str) == 36, "UUID should be 36 characters long"
    
    # Check UUID format using regex
    uuid_pattern = r'^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$'
    assert re.match(uuid_pattern, uuid_str), "UUID does not match expected format"

def test_uuid_uniqueness():
    """Test that multiple generated UUIDs are unique."""
    uuids = set(generate_uuid() for _ in range(1000))
    assert len(uuids) == 1000, "Generated UUIDs should be unique"

def test_uuid_version():
    """Verify the generated UUID is version 4 (random)."""
    uuid_str = generate_uuid()
    
    # Version is the 3rd character in the 3rd group
    version = uuid_str.split('-')[2][0]
    assert version == '4', "UUID should be version 4 (random)"