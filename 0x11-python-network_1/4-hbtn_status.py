#!/usr/bin/python3
""" Fetches https://intranet.hbtn.io/status"""
import requests


if __name__ == '__main__':
    s = requests.Session()

    response = s.get('https://intranet.hbtn.io/status')
    body = response.text

    print('Body response:')
    print('\t- type: {}'.format(type(body)))
    print('\t- content: {}'.format(body))
