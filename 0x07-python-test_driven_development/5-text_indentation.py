#!/usr/bin/python3
"""
Script defining a function text_indentation for sake of learning
to test through using doctest and unittest
"""


def text_indentation(text):
    """
    Prints text with extra lines for each '.', ':', '?' char

    Args:
    text -- The text to be printed
    """

    if type(text) is not str:
        raise TypeError("text must be a string")

    for delim in ".:?":
        text = (delim + "\n\n").join(
            [line.strip(" ") for line in text.split(delim)])

    print("{}".format(text), end="")
