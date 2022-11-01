#!/usr/bin/python3
"""
Return subscribers
"""
from requests import get
from sys import argv


def number_of_subscribers(subreddit):
    """ Return subscribers """
    head = {'User-Agent': 'Avery Harper'}
    count = get('https://www.reddit.com/r/{}/about.json'.format(
        subreddit), headers=head).json()
    try:
        return count.get('data').get('subscribers')
    except Exception:
        return 0


if __name__ == "__main__":
    number_of_subscribers(argv[1])
