#!/usr/bin/python3
'''Recursive function that queries the Reddit API, parses the title of all
hot articles, and prints a sorted count of given keywords'''

import requests


def count_words(subreddit, word_list, after=None, counts={}):
    '''Function to count occurrences of keywords in hot articles titles'''

    # Base case: when all posts have been processed
    if after == "":
        sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
        for word, count in sorted_counts:
            print(f"{word}: {count}")
        return

    # Set the URL and headers
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {
        "User-Agent": "linux:sm.api.advanced:v1.0.0 (by /u/sm_grit)"
    }

    # Define the parameters for the API request
    params = {'limit': 100, 'after': after}

    try:
        # Send the request to Reddit API
        response = requests.get(url, headers=headers,
                                params=params, allow_redirects=False)

        # Check for successful response
        if response.status_code == 200:
            data = response.json()
            posts = data.get("data", {}).get("children", [])

            # Process each post
            for post in posts:
                title = post.get("data", {}).get("title", "").lower()

                # Count occurrences of keywords in the title
                for word in word_list:
                    if title.count(word.lower()) > 0:
                        counts[word.lower()] = counts.get(word.lower(), 0) + 1

            # Call the function recursively with the next page's after value
            count_words(subreddit, word_list, data.get(
                        "data", {}).get("after"), counts)
        elif response.status_code == 404:
            print(None)
        else:
            print(None)
    except requests.RequestException:
        print(None)
