#!/usr/bin/python3
""" Script that fetches https://alx-intranet.hbtn.io/status """
import requests as r


response = r.get("https://alx-intranet.hbtn.io/status")
content = response.content.decode("utf-8")
print("Body response:")
print(f"\t- type: {type(content)}")
print(f"\t- content: {content}")
