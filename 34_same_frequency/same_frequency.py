def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """

    first_count = {}
    second_count = {}
    
    for x in str(num1):
        first_count[x] = first_count.get(x, 0) + 1
    
    for y in str(num2):
        second_count[y] = second_count.get(y, 0) + 1

    return    first_count == second_count 