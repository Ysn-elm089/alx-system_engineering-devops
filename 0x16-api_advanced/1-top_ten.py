#!/usr/bin/python3
"""
Script that queries the top 10 hot posts from a given Reddit subreddit.
"""

import requests

def top_ten(subreddit):
    """Print the titles of the first 10 hot posts listed for a given subreddit.
    
    Args:
        subreddit (str): The name of the subreddit to query.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers, allow_redirects=False)
    
    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']
        
        for post in posts[:10]:
            print(post['data']['title'])
    else:
        print("None")
