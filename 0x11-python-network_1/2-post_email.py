#!/usr/bin/python3
""" script that takes in a URL and an email
    sends a POST request to the passed URL with
    the email as a parameter and displays the body
    of the response (decoded in utf-8) """
import urllib.request as req
import urllib.parse as parse
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    email = {"email": sys.argv[2]}
    data = parse.urlencode(email).encode("ascii")

    with req.urlopen(url=url, data=data) as resposne:
        print(response.read().decode("utf-8"))


