#!/usr/bin/python3
""" Script to get the first 10 hot
    posts on Reddit
"""
import requests

def top_ten(subreddit):
    url = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=10'
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print(None)
        return

    posts = response.json().get('data', {}).get('children', [])
    for post in posts:
        print(post['data']['title'])

