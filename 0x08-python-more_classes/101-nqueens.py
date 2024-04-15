#!/usr/bin/python3
import sys as s

""" Script that lists the solutions of the N queens problem """

av = s.argv
ac = len(av)

# For invalid number of arguments
if ac != 2:
    print("Usage: nqueens N")
    s.exit(1)

# If N isn't an integer
elif not isinstance(int(av[1]), int):
    print("N must be a number")
    s.exit(1)

# If N is less than 4
elif int(av[1]) < 4:
    print("N must be at least 4")
    s.exit(1)

N = int(av[1])
chess_board = [[i, j] for i in range(N) for j in range(N)]
solutions = []

# Iterate over indices
# Choose a random
# Get the solutions


