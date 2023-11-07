#!/usr/bin/python3
""" Returns the number of subscribers in given subreddit"""
import requests


def number_of_subscribers(subreddit):
    """ Returns the subscribers """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'User-Agent': 'CustomUserAgent'}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        return (data['data']['subscribers'])
    else:
        return (0)
