#!/usr/bin/python3
"""
Script that queries subscribers on a given Reddit subreddit.
"""

import requests


def number_of_subscribers(subreddit):
    """Return the total number of subscribers on a given subreddit.
    
    Args:
        subreddit (str): The name of the subreddit to query.
        
    Returns:

 int: The number of subscribers if valid subreddit, otherwise 0.
    """
    if not subreddit or not isinstance(subreddit, str):
        return 0

    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "Mozilla/5.0"}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            return data['data']['subscribers']
        else:
            return 0
    except requests.RequestException:
        return 0




if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Please provide a subreddit name.")
    else:
        subreddit = sys.argv[1]
        print(number_of_subscribers(subreddit))
