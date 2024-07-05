#!/usr/bin/python3
""" script that takes in a URL
    sends a request to the URL and displays
    the body of the response (decoded in utf-8). """
import urllib.request as req
import urllib.error as err
import sys


if __name__ == "__main__":
    url = sys.argv[1]

    request = req.Request(url)
    try:
        with req.urlopen(request) as response:
            print(response.read().decode("utf-8"))
    except err.HTTPError as e:
        print(f"Error code: {e.code}")
