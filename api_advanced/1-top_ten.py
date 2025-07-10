#!/usr/bin/python3
import requests

def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first 10 hot posts for a given subreddit.
    
    Args:
        subreddit (str): The name of the subreddit to query
        
    Returns:
        None: Prints the titles or None if subreddit is invalid
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {'User-Agent': 'python:subreddit.hot.posts:v1.0 (by /u/yourusername)'}  # Custom User-Agent
    
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        
        # Check if the response is successful (status code 200)
        if response.status_code == 200:
            data = response.json()
            posts = data['data']['children']
            
            if not posts:
                print(None)
            else:
                for post in posts:
                    print(post['data']['title'])
        else:
            print(None)
    except requests.RequestException:
        print(None)
