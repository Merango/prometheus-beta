import pytest
from src.football_match_winner import determine_match_winner

def test_team1_wins():
    """Test when Team 1 wins by scoring more goals."""
    assert determine_match_winner(11, 11, 3, 2) == 'Team 1'

def test_team2_wins():
    """Test when Team 2 wins by scoring more goals."""
    assert determine_match_winner(11, 11, 2, 3) == 'Team 2'

def test_draw():
    """Test when the match ends in a draw."""
    assert determine_match_winner(11, 11, 2, 2) == 'Draw'

def test_invalid_negative_inputs():
    """Test handling of negative input values."""
    with pytest.raises(ValueError, match="All inputs must be non-negative integers"):
        determine_match_winner(-1, 11, 2, 2)
        determine_match_winner(11, -1, 2, 2)
        determine_match_winner(11, 11, -1, 2)
        determine_match_winner(11, 11, 2, -1)

def test_zero_players():
    """Test handling of teams with zero players."""
    with pytest.raises(ValueError, match="Both teams must have at least one player"):
        determine_match_winner(0, 11, 2, 2)
        determine_match_winner(11, 0, 2, 2)

def test_float_inputs():
    """Test handling of non-integer inputs."""
    with pytest.raises(ValueError, match="All inputs must be non-negative integers"):
        determine_match_winner(11.5, 11, 2, 2)
        determine_match_winner(11, 11.5, 2, 2)
        determine_match_winner(11, 11, 2.5, 2)
        determine_match_winner(11, 11, 2, 2.5)