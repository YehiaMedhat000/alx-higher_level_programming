#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argc = len(sys.argv) - 1
    if argc == 1:
        print("{} argument:".format(argc))
    elif argc == 0:
        print("{} arguments.".format(argc))
    else:
        print("{} arguments:".format(argc))

    if argc >= 1:
        argc = 1
        for arg in sys.argv[1:]:
            print("{}: {}".format(argc, arg))
            argc += 1
