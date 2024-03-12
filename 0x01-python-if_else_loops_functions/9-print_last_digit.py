#!/usr/bin/python3
def print_last_digit(number):
    ld = number if number > 0 else -number % 10
    print(ld, end="")
    return (ld)
