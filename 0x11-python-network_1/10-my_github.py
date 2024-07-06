#!/usr/bin/python3
""" script that takes your GitHub credentials
    (username and password) and uses the GitHub API to display your id """
import requests as r
from requests.auth import HTTPBasicAuth
import sys


if __name__ == "__main__":

    user = sys.argv[1]
    passwd = sys.argv[2]

    url = "https://api.github.com/user"
    
    # Sending the request
    auth = HTTPBasicAuth(user, passwd)
    response = r.get(url, auth=auth)
    print(response.json().get("id"))
