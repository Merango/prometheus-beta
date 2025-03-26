import pytest
from src.staircase_climber import climb_stairs

def test_climb_stairs_zero_steps():
    """Test climbing zero steps."""
    assert climb_stairs(0) == 1

def test_climb_stairs_one_step():
    """Test climbing one step."""
    assert climb_stairs(1) == 1

def test_climb_stairs_two_steps():
    """Test climbing two steps."""
    assert climb_stairs(2) == 2

def test_climb_stairs_three_steps():
    """Test climbing three steps."""
    assert climb_stairs(3) == 3

def test_climb_stairs_five_steps():
    """Test climbing five steps."""
    assert climb_stairs(5) == 8

def test_climb_stairs_ten_steps():
    """Test climbing ten steps."""
    assert climb_stairs(10) == 89

def test_climb_stairs_negative_steps():
    """Test that negative steps raise a ValueError."""
    with pytest.raises(ValueError, match="Number of steps cannot be negative"):
        climb_stairs(-1)

def test_climb_stairs_large_number():
    """Test climbing a larger number of steps."""
    assert climb_stairs(20) == 10946