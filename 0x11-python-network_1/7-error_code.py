#!/usr/bin/python3
""" script that takes in a URL
    sends a request to the URL
    and displays the body of the response. """
import requests as r
import sys


if __name__ == "__main__":
    # Get the url
    url = sys.argv[1]

    # Fetch using get
    response = r.get(url)
    if response.status_code >= 400:
        print(f"Error code: {response.status_code}")
    else:
        print(response.text)
