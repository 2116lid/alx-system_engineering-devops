#!/usr/bin/python3
"""function that queries the Reddit API
and returns the number of subscribers
"""
import requests


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of subscribers,
    Returns 0 if the subreddit is invalid or non-existent.
    """

    headers = {'User-Agent': 'MyRedditAPIWrapper/1.0 (by /u/bdov_)'}
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    response = requests.get(url, headers=headers)
    if response.status_code == 200 and response.json()['name'] == subreddit:
        subscribers = response.json()['data']['subscribers']
        return subscribers
    else:
        return 0
