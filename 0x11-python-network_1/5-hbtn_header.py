#!/usr/bin/python3
""" script that takes in a URL
    sends a request to the URL and displays the value of
    the variable X-Request-Id in the response header """
import requests as r
import sys


url = sys.argv[1]
response = r.get(url)
print(response.headers["X-Request-Id"])
