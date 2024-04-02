#!/usr/bin/python3
"""
    Defines class called Square
"""


class Square:
    """
        The definition of the square class

        Attributes:
            size: The side length of the square
    """
    def __init__(self, size=0) -> None:
        self.__size = size

        if self.__size < 0:
            raise TypeError("size must be an integer")
        elif not isinstance(size, int):
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
