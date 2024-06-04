#!/usr/bin/python3
'''
Recursive function that queries the Reddit API,
parses the title of all hot articles, and prints
a sorted count of given keywords
'''

import requests


def count_words(subreddit, word_list, sorted_count={}, after="", count=0):
    '''
    Function to count occurrences of keywords in hot articles titles.
    '''

    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": "linux:sm.api.advanced:v1.0.0 (by /u/sm_grit)"
    }

    params = {
        "after": after,
        "count": count,
        "limit": 100
    }

    response = requests.get(
                url, headers=headers, params=params, allow_redirects=False)

    try:
        results = response.json()
        if response.status_code == 404:
            raise Exception
    except Exception:
        print("")
        return

    results = results.get("data")
    after = results.get("after")
    count += results.get("dist")

    for c in results.get("children"):
        title = c.get("data").get("title").lower().split()
        for word in word_list:
            if word.lower() in title:
                times = len([t for t in title if t == word.lower()])
                if sorted_count.get(word) is None:
                    sorted_count[word] = times
                else:
                    sorted_count[word] += times

    if after is None:
        if len(sorted_count) == 0:
            print("")
            return
        sorted_count = sorted(
                        sorted_count.items(), key=lambda kv: (-kv[1], kv[0]))
        for k, v in sorted_count:
            print("{}: {}".format(k, v))
    else:
        count_words(subreddit, word_list, sorted_count, after, count)
