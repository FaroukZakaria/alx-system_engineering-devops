#!/usr/bin/python3
""" Returns the top 10 posts in given subreddit"""
import requests


def top_ten(subreddit):
    """ Returns the hot lists """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'CustomUserAgent'}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        if 'children' in data['data']:
            for post in data['data']['children'][:10]:
                print(post['data']['title'])
    else:
        print(None)
