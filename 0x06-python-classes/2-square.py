#!/usr/bin/python3
"""
    Defines class called Square
"""


class Square:
    """
        The definition of the square class
    """
    def __init__(self, size=0) -> None:
        self.__size = size

        if self.__size < 0:
            raise ValueError("size must be >= 0")
        elif not isinstance(size, int):
            raise TypeError("size must be an integer")
