#!/usr/bin/python3
""" Module defining Rectangle class based on
    `BaseGeometry` class
"""
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """ Class Definition `Rectangle` """

    def __init__(self, width, height):
        """ Initialization function
            called whenever a new instance of `Rectangle` is made

            Args:
                self -- The object
                width -- The width of the object
                height -- The height of the object
        """
        super().__init__()
        self.integer_validator('width', width)
        self.__width = width
        self.integer_validator('height', height)
        self.__height = height
