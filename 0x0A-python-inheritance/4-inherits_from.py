#!/usr/bin/python3
""" Module defining `inherits_from` function """


def inherits_from(obj, a_class):
    """ inherits_from
        Function that checks if obj
        is an instance of a_class and not other inherited classes

        Args:
            obj -- The object to be checked
            a_class -- The class to be checked against
        Return:
            True if obj is an instance of a_class
            False if obj isn't an instance of a_class
    """

    return isinstance(obj, a_class) and type(obj) is not a_class
