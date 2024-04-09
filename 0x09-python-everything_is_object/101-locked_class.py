#!/usr/bin/python3
"""
Class definition that prevents creating attributes
"""


class LockedClass:
    """
    LockedClass class definition
    Accepts only the attribute `first_name`
    """
    __slots__ = ["first_name"]
