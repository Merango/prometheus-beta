def find_word_occurrences(input_string: str, target_word: str) -> list:
    """
    Find all occurrences of a target word in a given string with their character positions.

    Args:
        input_string (str): The string to search in
        target_word (str): The word to find occurrences of

    Returns:
        list: A list of tuples, each containing the character position and the occurrence of the word

    Raises:
        ValueError: If input_string or target_word is empty
        TypeError: If inputs are not strings
    """
    # Validate inputs
    if not isinstance(input_string, str) or not isinstance(target_word, str):
        raise TypeError("Both input_string and target_word must be strings")
    
    if not input_string or not target_word:
        raise ValueError("Input string and target word cannot be empty")

    # Split the input string into words
    words = input_string.split()
    
    # Store results
    occurrences = []
    
    # Track cumulative character count
    current_position = 0
    
    # Iterate through words
    for i, word in enumerate(words):
        # Check if current word matches target
        if word == target_word:
            occurrences.append((current_position, word))
        
        # Update current position 
        # Add word length plus space for all words except the last one
        current_position += len(word) + (1 if i < len(words) - 1 else 0)
    
    return occurrences