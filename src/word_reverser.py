def reverse_words(sentence):
    """
    Reverse the order of words in a string while maintaining original capitalization and punctuation.
    
    Args:
        sentence (str): The input string to be processed.
    
    Returns:
        str: A string with words reversed, preserving original capitalization and punctuation.
    
    Examples:
        >>> reverse_words("Hello World!")
        'World Hello!'
        >>> reverse_words("Python is AWESOME.")
        'AWESOME is Python.'
        >>> reverse_words("a,b c")
        'c,b a'
    """
    # Handle edge cases
    if not sentence:
        return ""
    
    # Split the sentence into words while preserving punctuation and whitespace
    def split_with_punctuation(s):
        words = []
        current_word = []
        for char in s:
            if char.isalnum():
                current_word.append(char)
            else:
                if current_word:
                    words.append(''.join(current_word))
                    current_word = []
                words.append(char)
        if current_word:
            words.append(''.join(current_word))
        return words
    
    # Separate words and non-word tokens
    tokens = split_with_punctuation(sentence)
    
    # Separate words from punctuation/spaces
    words = [token for token in tokens if token.isalnum()]
    non_words = [token for token in tokens if not token.isalnum()]
    
    # Reverse the words
    words = list(reversed(words))
    
    # Reconstruct the sentence
    result = []
    word_index = 0
    for token in tokens:
        if token.isalnum():
            result.append(words[word_index])
            word_index += 1
        else:
            result.append(token)
    
    return ''.join(result)