#!/usr/bin/python3
""" Module defining `is_kind_of_class` function """


def is_kind_of_class(obj, a_class):
    """ is_kind_of_class
        Function that checks if obj
        is an instance of a_class or another inherited class

        Args:
            obj -- The object to be checked
            a_class -- The class to be checked against
        Return:
            True if obj is an instance of a_class
            False if obj isn't an instance of a_class
    """

    return isinstance(obj, a_class)
