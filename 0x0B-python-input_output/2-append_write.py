#!/usr/bin/python3
""" Module defining the function `` """


def append_write(filename="", text=""):
    """ function that appends a string at the end of a text file (UTF8)
        and returns the number of characters added:

        Args:
            filename -- The file's name to be appended to
            text -- The buffer to be appended to the file
            called filename

        Returns:
            The number of appended characters from text
            to the file
    """
    with open(filename, "a", encoding="UTF-8") as f:
        return f.write(text)
