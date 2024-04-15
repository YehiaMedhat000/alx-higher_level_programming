#!/usr/bin/python3
""" Module defining `is_same_class` function """


def is_same_class(obj, a_class):
    """ is_same_class
        Function that checks if obj
        is an instance of a_class

        Args:
            obj -- The object to be checked
            a_class -- The class to be checked against
        Return:
            True if obj is an instance of a_class
            False if obj isn't an instance of a_class
    """

    return type(obj) is a_class
