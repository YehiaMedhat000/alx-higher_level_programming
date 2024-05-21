#!/usr/bin/python3
""" Definition of the `Rectangle` class """
from models.base import Base


class Rectangle(Base):
    """ Definition of the `Rectangle` class
        Inherits from `Base`
    """

    @staticmethod
    def validate(**kwargs):
        """ Function to validate the values """
        for k, v in kwargs.items():
            if not isinstance(v, int):
                raise TypeError(f"{k} must be an integer")

            elif k in {"width", "height"} and v <= 0:
                raise ValueError(f"{k} must be > 0")

            elif k in {"x", "y"} and v < 0:
                raise ValueError(f"{k} must be >= 0")

    def __init__(self, width, height, x=0, y=0, id=None):
        """ The init method for the Rectangle class
            Or the constructor method

            Args:
                self -- The object its self
                width -- The width
                height -- The height
                x -- The x coordinate
                y -- The y coorediante
                id -- The ID of the object
        """
        super().__init__(id)

        kwargs = {
            "width": width,
            "height": height,
            "x": x,
            "y": y
        }

        Rectangle.validate(**kwargs)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """ Getter method for width """
        return self.__width

    @property
    def height(self):
        """ Getter method for height """
        return self.__height

    @property
    def x(self):
        """ Getter method for x """
        return self.__x

    @property
    def y(self):
        """ Getter method for y """
        return self.y

    @width.setter
    def width(self, width):
        """ Setter method for width """
        Rectangle.validate(**{"width": width})
        self.__width = width

    @height.setter
    def height(self, height):
        """ Setter method for height """
        Rectangle.validate(**{"height": height})
        self.__height = height

    @x.setter
    def x(self, x):
        """ Setter method for x """
        Rectangle.validate(**{"x": x})
        self.__x = x

    @y.setter
    def y(self, y):
        """ Setter method for y """
        Rectangle.validate(**{"y": y})
        self.__y = y

    def area(self):
        """ Method to compute area of the rectangle """
        return self.__width * self.__height

    def display(self):
        """ Method for printing the rectangle
            as a two dimensional shape in the stdout
        """
        for _ in range(self.__y):
            print()
        for _ in range(self.__height):
            print(' ' * self.__x, end='')
            print('#' * self.__width)

    def __str__(self):
        """ Method that returns some information
            about the rectangle object
        """
        first = f" - {self.__width}/{self.__height}"
        second = f" ({self.id}) {self.__x}/{self.__y}"
        return ("[Rectangle]" + second + first)

    def update(self, *args, **kwargs):
        """ Method to update the values
            of the object self

            Args:
                args -- The arguments to change
                in order as follows:
                id, width, height, x, y
        """
        if args != None and len(args) != 0:
            list_atr = ['id', 'width', 'height', 'x', 'y']
            for i in range(len(args)):
                setattr(self, list_atr[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """ Method for returning the dictionary
            representation of the object self
        """
        return {"width": self.width, "height": self.height,
                "x": self.x, "y": self.y, "id": self.id}
