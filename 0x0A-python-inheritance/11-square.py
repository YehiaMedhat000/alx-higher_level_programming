#!/usr/bin/python3
""" Module defining Square class based on
    `Rectangle` class
"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """ Definition of the `Square` class """

    def __init__(self, size):
        super().__init__(size, size)
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """ Method to compute the area of the Square object

            Args:
                self -- The Square to get the area

            Returns:
                The area of the Square object
        """
        return self.__size ** 2

    def __str__(self):
        """ Returns the string representation
            of the object

            Args:
                self -- The square object

            Returns:
                The string representation of the object
        """
        return "[Square] {}/{}".format(self.__size, self.__size)
