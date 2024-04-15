#!/usr/bin/python3
""" Module defining the `MyInt` class """


class MyInt(int):
    """ `MyInt` class definition """

    def __eq__(self, other):
        """ Method for the equality operator """
        return other.__ne__(self)

    def __ne__(self, other):
        """ Method for the inequality operator """
        return other.__eq__(self)
