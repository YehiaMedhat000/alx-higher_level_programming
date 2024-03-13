#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    result = 0
    argc = len(sys.argv) - 1
    for arg in sys.argv[1:]:
        result += int(arg)
    print(result)
