#!/usr/bin/python3
""" Module defining a funciton `read_file` """


def read_file(filename=""):
    """ function that reads a text file (UTF8)
        and prints it to stdout:

        Args:
            filename -- The filename to read and print
    """
    with open(filename, "r", encoding="UTF-8") as f:
        print(f.read(), end="")
