def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    flipped_phrase = "";
    for letter in phrase:
        if to_swap.lower() in letter.lower() and letter.isupper():
            flipped_phrase = flipped_phrase + letter.lower();
        elif to_swap.lower() in letter.lower() and letter.islower():
            flipped_phrase = flipped_phrase + letter.upper();
        else:
            flipped_phrase = flipped_phrase + letter;
    
    return flipped_phrase;

    """
    simpler answer:
    to_swap = to_swap.lower()
    out = ""

    for ltr in phrase:
        if ltr.lower() == to_swap:
            ltr = ltr.swapcase()
        out += ltr

    return out
    """