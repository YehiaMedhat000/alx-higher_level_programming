#!/usr/bin/python3
def uppercase(str):
    for c in str:
        if 122 >= ord(c) >= 97:
            c = chr(ord(c) - 32)
        print("{}".format(c), end="")
    print("")

uppercase("this is very cool")
