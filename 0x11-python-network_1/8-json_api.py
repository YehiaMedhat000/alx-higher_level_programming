#!/usr/bin/python3
""" script that takes in a letter and sends a POST request
    to http://0.0.0.0:5000/search_user with the letter as a parameter. """
import requests as r
import sys


if __name__ == "__main__":

    ac = len(sys.argv)
    if ac == 2:
        letter = {'q': sys.argv[1]}

        # Handling the request
        response = r.post(url="http://0.0.0.0:5000/search_user", data=letter)
        info = response.json()

        # Getting output
        size = len(info)
        if size == 0:
            print("No result")
        else:
            print(f"[{info['id']}] {info['name']}")

    else:
        print("No result")
