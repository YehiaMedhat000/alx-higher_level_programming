#!/usr/bin/python3
""" Module defining a function `write_file` """


def write_file(filename="", text=""):
    """ function that writes a string to a text file (UTF8)
        and returns the number of characters written

        Args:
            filename -- The filename to write to
            text -- The buffer to write and save into
            the file called filename
        Returns:
            The number of characters written
    """
    with open(filename, "w", encoding="UTF-8") as f:
        return f.write(text)
