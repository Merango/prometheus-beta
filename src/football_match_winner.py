def determine_match_winner(team1_players, team2_players, team1_goals, team2_goals):
    """
    Determine the winner of a football match based on players and goals.
    
    Args:
        team1_players (int): Number of players on team 1
        team2_players (int): Number of players on team 2
        team1_goals (int): Number of goals scored by team 1
        team2_goals (int): Number of goals scored by team 2
    
    Returns:
        str: Winner of the match ('Team 1', 'Team 2', or 'Draw')
    
    Raises:
        ValueError: If input values are invalid
    """
    # Validate inputs
    if not all(isinstance(x, int) and x >= 0 for x in [team1_players, team2_players, team1_goals, team2_goals]):
        raise ValueError("All inputs must be non-negative integers")
    
    # If either team has 0 players, raise an error
    if team1_players == 0 or team2_players == 0:
        raise ValueError("Both teams must have at least one player")
    
    # If goals are equal, it's a draw
    if team1_goals == team2_goals:
        return 'Draw'
    
    # Team with more goals wins
    return 'Team 1' if team1_goals > team2_goals else 'Team 2'