#!/usr/bin/python3
def add_integer(a, b=98):
    """
    Addition function

    Args:
        a: integer, or float
        b: integer, or float

    Return:
        The sum of integer a and integer b
    """

    ta = type(a)
    tb = type(b)
    if ta != int and ta != float:
        raise TypeError("a must be an integer")
    elif tb != int and tb != float:
        raise TypeError("b must be an integer")

    return (int(a) + int(b))
