#!/usr/bin/python3
""" Module for the last task in the
    0x0B-python-Input_output project
"""
from sys import stdin


codes = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0,
}

size = i = 0


def out():
    """ Prints the status code/s that is/are not
        assigned to 0
    """
    print(f"File size: {size}")
    for key, val in sorted(codes.items()):
        if val != 0:
            print("{:s}: {:d}".format(key, val))


try:
    for line in stdin:
        parsed = line.split()
        if len(parsed) >= 2:
            status = parsed[-2]
            size += int(parsed[-1])
            if status in codes:
                codes[status] += 1
        i += 1

        if i % 10 == 0:
            out()
    out()
except KeyboardInterrupt:
    out()
