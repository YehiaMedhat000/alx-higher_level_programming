#!/usr/bin/python3
""" Script that lists 10 commits using the Github api
    from newest to oldest """
import requests as r
import sys


if __name__ == "__main__":

    repo = sys.argv[1]
    owner = sys.argv[2]
    headers = {"owner": owner, "repo": repo}

    url = f"https://api.github.com/repos/{owner}/{repo}/commits"

    response = r.get(url, headers=headers)
    commits = response.json()

    try:
        for i in range(10):
            sha = commits[i].get("sha")
            committer = commits[i]["commit"]["author"]["name"]
            print(f"{sha}: {committer}")
    except IndexError:
        pass
