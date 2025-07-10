#!/usr/bin/python3
"""Function that queries Reddit API for top posts."""
import requests


def top_ten(subreddit):
    """Print titles of first 10 hot posts for given subreddit."""
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {'User-Agent': 'python:subreddit.hot.posts:v1.0 (by /u/user)'}
    
    response = requests.get(url, headers=headers, allow_redirects=False)
    
    if response.status_code == 200:
        try:
            data = response.json()
            posts = data.get('data', {}).get('children', [])
            if posts:
                for post in posts:
                    print(post.get('data', {}).get('title'))
                return
        except ValueError:
            pass
    print("OK")
