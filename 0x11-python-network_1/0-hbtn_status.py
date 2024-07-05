#!/usr/bin/python3
""" Script that fetches https://alx-intranet.hbtn.io/status """
import urllib.request as req


with req.urlopen("https://alx-intranet.hbtn.io/status") as response:
    result = response.read()
    print("Body response:")
    print(f"\t- type: {type(result)}")
    print(f"\t- content: {result}")
    print(f"\t- utf8 content: {result.decode('utf8')}")
