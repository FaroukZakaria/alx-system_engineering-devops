#!/usr/bin/python3
""" sorted count on given keywords """
import requests
from collections import Counter


def count_words(subreddit, word_list, after=None, word_counts=None):
    if word_counts is None:
        word_counts = Counter()

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'CustomUserAgent'}
    params = {'after': after} if after else {}

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()

        if 'children' in data['data']:
            for post in data['data']['children']:
                title = post['data']['title'].lower()
                title_words = title.split()
                for word in word_list:
                    if any(
                            title_word.startswith(word) and
                            title_word[len(word):].isalpha() is False
                            for title_word in title_words
                            ):
                        word_counts[word] += 1

            next_after = data['data']['after']
            if next_after:
                count_words(
                        subreddit, word_list,
                        after=next_after, word_counts=word_counts
                        )
            else:
                for word, count in sorted(
                        word_counts.items(), key=lambda x: (-x[1], x[0])
                        ):
                    print(f"{word}: {count}")
        else:
            pass
    elif response.status_code == 404:
        pass
    else:
        pass

# count_words("learnprogramming", ["java", "python", "javascript"])
