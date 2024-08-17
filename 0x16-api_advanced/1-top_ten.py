#!/usr/bin/python3
"""
    Uses reddit API to get 10 hot posts
"""
import requests


def top_ten(subreddit):
    """Get 10 hot posts"""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {'user-agent': 'request'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        print(None)
        return 0

