#!/usr/bin/python3
"""Script that fetches 10 hot posts for a given subreddit."""
import requests

def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts for a valid subreddit.
    If not valid, prints None."""
    
    headers = {'User-Agent': 'MyAPI/0.0.1'}
    url = f"https://reddit.com/r/{subreddit}/hot.json"
    
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)

        if response.status_code != 200:
            print(None)
            return

        data = response.json().get('data', {}).get('children', [])
        if not data:
            print(None)
            return

        for post in data[:10]:
            print(post.get('data', {}).get('title'))

    except Exception:
        print(None)
