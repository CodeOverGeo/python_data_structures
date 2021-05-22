def vowel_count(phrase):
    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}
        
        >>> vowel_count('HOW ARE YOU? i am great!') 
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """
    vowels = set(['a', 'e', 'i', 'o', 'u'])
    vowel_freq = {}
    for char in phrase:
        lowchar = char.lower()
        if lowchar in vowels:
            vowel_freq[lowchar] = vowel_freq.get(lowchar, 0) + 1 
    return vowel_freq