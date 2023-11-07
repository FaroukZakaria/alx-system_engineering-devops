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
        if 'children' in data['data']:
            for post in data['data']['children'][:10]:
                print(post['data']['title'])
    else:
        print(None)
