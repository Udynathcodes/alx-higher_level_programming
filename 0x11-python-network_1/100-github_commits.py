#!/usr/bin/python3
"""
List 10 commits froma repo
"""

import requests
from requests import get
import sys


if __name__ == "__main__":
    repo = sys.argv[1]
    owner = sys.argv[2]
    url = "https://api.github.com/repos/{}/{}/commits".format(owner, repo)

    response = requests.get(url)

    json_data = response.json()

    count = 1

    for info in json_data:
        if count > 10:
            break
        sha = info.get('sha')
        author = info.get('commit').get('author').get('name')
        print("{}: {}".format(sha, author))
        count += 1
