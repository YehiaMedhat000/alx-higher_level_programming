#!/usr/bin/python3
"""
Script defining a function say_my_name for sake of learning
to test through using doctest and unittest
"""


def say_my_name(first_name, last_name=""):
    """
    Prints simple sentence

    Args:
    first_name -- The first name to be used
    last_name -- The second name to be used
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
