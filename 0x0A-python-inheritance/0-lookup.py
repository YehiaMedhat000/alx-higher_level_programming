#!/usr/bin/python3
""" Function definition
    Task.0 """


def lookup(obj):
    """
    Looks up object attributes and methods

    Args:
    obj -- The object to get its attributes and methods

    Returns:
    List of all methods and attributes of obj
    """
    return dir(obj)
