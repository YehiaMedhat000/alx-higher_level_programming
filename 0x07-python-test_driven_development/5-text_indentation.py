#!/usr/bin/python3
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
            print(text[old+2:i+1])
            print()
            old = i
