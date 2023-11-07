#!/usr/bin/python3
""" Recursive approach """
import requests


def recurse(subreddit, hot_list=None, after=None):
    """ Recursively gets titles of all hot articles """
    if hot_list is None:
        hot_list = []

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'CustomUserAgent'}
    params = {'after': after} if after else {}
    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()

        if 'children' in data['data']:
            for post in data['data']['children']:
                hot_list.append(post['data']['title'])

            next_after = data['data']['after']
            if next_after:
                recurse(subreddit, hot_list, after=next_after)
            else:
                return hot_list
        else:
            return None
    else:
        return None
