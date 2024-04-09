#!/usr/bin/python3
""" Script that defines a class rectangle """


class Rectangle:
    """ Definition of the class """

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    def __str__(self):
        """
        Returns string visulaization of the rectangle
        Using the # characters
        """

        str = ""
        for row in range(self.__height):
            for col in range(self.__width):
                str += '#'
            if self.__width != 0 and row < (self.__height - 1):
                str += '\n'
        return str

    def __repr__(self):
        """
        Returns the code for recreating a rectangle instance
        with the same dimensions
        """

        return ('Rectangle({}, {})'.format(self.__width, self.__height))

    def __del__(self):
        """
        Deletes an instance of the class
        with printing the message "Bye rectangle..."
        """

        del (self)
        print("Bye rectangle...")

    @property
    def width(self):
        """
        Getter method for __width

        Returns: The property __width
        """

        return self.__width

    @width.setter
    def width(self, width):
        """
        Setter method for __width
        """

        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

    @property
    def height(self):
        """
        Getter method for __height

        Returns: The property __height
        """

        return self.__height

    @height.setter
    def height(self, height):
        """
        Setter method for __height
        """

        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height

    def area(self):
        """
        Gets the area of the rectangle
        """

        return (self.__width * self.__height)

    def perimeter(self):
        """
        Gets the perimeter of the rectangle
        """

        if self.__width == 0 or self.__height == 0:
            return 0
        return ((self.__width + self.__height) * 2)
