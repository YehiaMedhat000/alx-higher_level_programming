#!/usr/bin/python3
def fizzbuzz():
    for i in range(1, 101):
        if not (i % 5) and not (i % 3):
            print("FizzBuzz", end=" ")
        elif not (i % 5):
            print("Buzz", end=" ")
        elif not (i % 3):
            print("Fizz", end=" ")
        else:
            print(i, end=" ")
