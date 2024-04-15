#!/usr/bin/python3
""" Module defining a function
    for adding a new attribute to some object
"""


def add_attribute(self, attr, val):
    """ `add_attribute` definition that attempts to
        add a new attribute to the self object

        Args:
            self -- The object to add the attribute to
            attr -- The name of the attribute
            val -- The value of the attribute

        Returns:
            None
    """
    if hasattr(self, "__dict__"):
        setattr(self, attr, val)
    else:
        raise TypeError("can't add new attribute")
