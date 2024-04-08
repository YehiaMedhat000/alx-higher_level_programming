#!/usr/bin/python3
def print_square(size):

    """
    Prints a square using the # char

    Args:
    size -- Integer side length of the square
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        for _ in range(size):
            print('#', end='')
        print()
