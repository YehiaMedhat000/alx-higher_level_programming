#!/usr/bin/python3
""" script that takes in a letter and sends a POST request
    to http://0.0.0.0:5000/search_user with the letter as a parameter. """
import requests as r
import sys


if __name__ == "__main__":

    ac = len(sys.argv)
    val = "" if ac == 1 else sys.argv[1]
    letter = {'q': val}

    # Handling the request
    response = r.post(url="http://0.0.0.0:5000/search_user", data=letter)
    try:
        info = response.json()
        if info == {}:
            print("No result")
        else:
            print(f"[{info['id']}] {info['name']}")

    except ValueError:
        print("Not a Valid JSON")
