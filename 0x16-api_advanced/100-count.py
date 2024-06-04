#!/usr/bin/python3
'''Recursive function that queries the Reddit API, parses the title of all
hot articles, and prints a sorted count of given keywords.'''
import requests


def count_words(subreddit, word_list, after=None, counts=None):
    '''Function to count occurrences of keywords in hot articles titles'''

    if counts is None:
        counts = {}

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
        "User-Agent": "linux:sm.api.advanced:v1.0.0 (by /u/sm_grit)"
    }

    params = {'limit': 100, 'after': after}

    try:
        response = requests.get(url, headers=headers,
                                params=params, allow_redirects=False)

        if response.status_code == 200:
            data = response.json().get("data", {})
            posts = data.get("children", [])

            if not posts:
                print("")
                return

            for post in posts:
                title = post.get("data", {}).get("title", "").lower()

                for word in word_list:
                    if title.count(word.lower()) > 0:
                        counts[word.lower()] = counts.get(word.lower(), 0) + 1

            after = data.get("after")
            if after:
                count_words(subreddit, word_list, after, counts)
            else:
                sorted_counts = sorted(
                                 counts.items(), key=lambda x: (-x[1], x[0]))
                for word, count in sorted_counts:
                    print("{}: {}".format(word, count))
        else:
            print("")
    except requests.RequestException:
        print("")
