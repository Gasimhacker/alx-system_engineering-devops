#!/usr/bin/python3
"""A script to count the number of subscribers in a subreddit"""

import requests


def number_of_subscribers(subreddit):
    """Count the number of subscribers"""
    headers = {'User-Agent': 'Chrome/124.0.0.0 Safari/537.36'}
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    r = requests.get(url, headers=headers)
    if (r.status_code == 404):
        return 0
    subreddit_data = r.json().get('data')
    return subreddit_data.get('subscribers')
