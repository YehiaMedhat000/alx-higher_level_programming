#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys as s

    ac = len(s.argv[1:])

    if ac != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        print(ac)
        print(s.argv)
        s.exit(1)

    a = int(s.argv[1])
    b = int(s.argv[3])

    match s.argv[2]:
        case '+':
            print("{} {} {} = {}".format(a, s.argv[2], b, add(a, b)))
        case '-':
            print("{} {} {} = {}".format(a, s.argv[2], b, sub(a, b)))
        case '*':
            print("{} {} {} = {}".format(a, s.argv[2], b, mul(a, b)))
        case '/':
            print("{} {} {} = {}".format(a, s.argv[2], b, div(a, b)))
        case _:
            print("Unknown operator. Available operators: +, -, * and /")
            s.exit(1)

