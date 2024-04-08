#!/usr/bin/python3
def print_square(size):

    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    # if size is a float and is less than 0
    # raise a TypeError exception with the message size must be an integer
    elif size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        for _ in range(size):
            print('#', end='')
        print()
