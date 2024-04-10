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
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    old = 0
    for i, char in enumerate(text):
        if char in ":.?":
            print(text[old:i+1])
            print()
            old = i + 2
