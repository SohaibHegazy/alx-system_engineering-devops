#!/usr/bin/python3
'''
a module that queries the Reddit API and returns
the number of subscribers (not active users, total
subscribers) for a given subreddit.
If an invalid subreddit is given, the function should return 0.
'''
import requests


def number_of_subscribers(subreddit):
    '''
    a function to get the total number of subscribers
    in Reddit, it returns 0 if invalid subbreddit is passed
    '''
    url = f"https://api.reddit.com/r/{subreddit}/about"
    headers = {'User-Agent': 'CustomClient/1.0'}
    response = requests.get(url, headers=headers, allow_redirects=False)
        
    if response.status_code != 200:
	return (0)
    response = response.json()
    if 'data' in response:
	return (response.get('data').get('subscribers'))
    else:
	return (0)
