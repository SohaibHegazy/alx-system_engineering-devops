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
    url = ("https://www.reddit.com/r/{}/about.json".format(subreddit))
    headers = {'User-Agent': 'Mozilla/5.0'}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            return data['data']['subscribers']
        else:
            return 0
    except requests.RequestException:
        return 0
