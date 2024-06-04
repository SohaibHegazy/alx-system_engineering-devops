#!/usr/bin/python3
'''Recursive function that queries the Reddit API and returns a list
containing the titles of all hot articles for a given subreddit'''

import requests


def recurse(subreddit, hot_list=[]):
    '''Recursive function to retrieve titles of all hot articles of a
    subreddit'''
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'linux:sm.api.advanced:v1.0.0 (by /u/sm_grit)'}
    params = {'limit': 100, 'after': hot_list[-1] if hot_list else None}

    try:
        response = requests.get(
            url, headers=headers, params=params, allow_redirects=False)

        if response.status_code == 200:
            data = response.json()
            posts = data.get('data', {}).get('children', [])
            if not posts:
                return hot_list
            hot_list.extend([post.get('data', {}).get('title', '')
                             for post in posts])
            return recurse(subreddit, hot_list)
        elif response.status_code == 404:
            return None
        else:
            return None
    except requests.RequestException:
        return None
