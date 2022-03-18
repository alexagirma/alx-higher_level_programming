#!/usr/bin/python3
""" Fetches https://intranet.hbtn.io/status"""
import requests
from requests.auth import HTTPBasicAuth
from sys import argv


if __name__ == '__main__':
    repo, user = argv[1:]
    url = 'https://api.github.com/repos/{}/{}/commits'.format(user, repo)

    s = requests.Session()

    response = s.get(url)
    commits = response.json()[:10]
    for commit in commits:
        print(commit.get('sha'), end=': ')
        print(commit.get('commit').get('author').get('name'))
