#!/usr/bin/python3
'''Function that queries the Reddit API and prints the titles of the first 10
hot posts listed for a given subreddit'''

import requests


def top_ten(subreddit):
    '''Function to print the titles of the first 10 hot posts of a subreddit'''
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {'User-Agent': 'linux:sm.api.advanced:v1.0.0 (by /u/sm_grit)'}

    try:
        response = requests.get(
            url, headers=headers, allow_redirects=False)

        if response.status_code == 200:
            data = response.json()
            posts = data.get('data', {}).get('children', [])
            if not posts:
                print(None)
            for post in posts:
                print(post.get('data', {}).get('title', ''))
        else:
            print(None)
    except requests.RequestException:
        print(None)
