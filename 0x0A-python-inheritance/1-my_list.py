#!/usr/bin/python3
""" Module defining Class Mylist """


class Mylist(list):
    """ Class definition
        Mylist

        Methods:
            print_sorted:
                Prints the list object sorted
    """

    def print_sorted(self):
        """ print_sorted
            Class method that prints a list object
            sorted ascendingly

            Args:
                self -- The list object
        """
        print(sorted(self))
