#!/usr/bin/python3
def print_last_digit(number):
    number = number if number > 0 else -number
    ld = number % 10
    print(ld, end="")
    return (ld)
