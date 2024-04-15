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

    def area(self):
        """ Method to compute the area
            of the rectangel object

            Args:
                self -- The rectangle object

            Returns:
                The area of the rectangle object
        """
        return (self.__width * self.__height)

    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
