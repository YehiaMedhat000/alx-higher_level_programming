#!/usr/bin/python3
""" Module defining the base class `Base` """


class Base:
    """ Class Base Definition """

    __nb_objects = 0

    def __init__(self, id=None):
        """ The class Constructor

            Args:
                id -- The id of the object created
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
