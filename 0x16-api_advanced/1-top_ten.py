#!/usr/bin/python3
"""a function that queries the Reddit api"""
import requests


def top_ten(subreddit):
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)

    api_headers = {
        'User-Agent': 'Chrome/126.0.0.0'
    }

    response = requests.get(url, headers=api_headers)

    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()
        posts = data['data']['children']
        for post in posts:
            print(post['data']['title'])
    else:
        print(None)
