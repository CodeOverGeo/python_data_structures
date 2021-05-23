def remove_every_other(lst):
    """Return a new list of other item.

        >>> lst = [1, 2, 3, 4, 5]

        >>> remove_every_other(lst)
        [1, 3, 5]

    This should return a list, not mutate the original:

        >>> lst
        [1, 2, 3, 4, 5]
    """

    newlst = lst[0::2]
    return newlst

    # [0:end:1] syntax defaults first index to 0, don't have to state
    # could have ran on one line