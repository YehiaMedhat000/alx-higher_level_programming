#!/usr/bin/python3
""" Module defining class `BaseGeometry` """


class BaseGeometry():
    """ Definition of class BaseGeometry """
    def area(self):
        """ Method `area`
            Computes the area of a shape

            Args:
                self -- The shape object argument
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ Method `integer_validator`
            Validates the value associated with the shape obj

            Args:
                self -- The shape object
                name -- The object's name
                value -- The object's value
            Returns:
                True if valud is valid
                False if valud is invalid
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
