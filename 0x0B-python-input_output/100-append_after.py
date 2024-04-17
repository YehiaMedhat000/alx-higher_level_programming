#!/usr/bin/python3
""" Module defining the function `append_after` """


def append_after(filename="", search_string="", new_string=""):
    """ function that inserts a line of text to a file
        after each line containing a specific string

        Args:
            filename -- The file's name to be manipulated
            search_string -- The string after which to append new_string
            new_string -- The string to be appended
    """
    with open(filename, 'r', encoding="UTF-8") as f:
        lines = []
        while True:
            line = f.readline()
            if line == "":
                break
            lines.append(line)
            if search_string in line:
                lines.append(new_string)
    with open(filename, 'w', encoding="UTF-8") as f:
        f.writelines(lines)
