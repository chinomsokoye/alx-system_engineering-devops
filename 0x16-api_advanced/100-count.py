#!/usr/bin/python3
"""
Print sorted counts of given keyword
"""
from requests import get
from sys import argv


hotlist = []
after = None


def count_words(subreddit, word_list):
    global hotlist
    global after
    """ Return sorted counts of given keywords """
    head = {'User-Agent': 'Avery Harper'}
    URL = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    parameters = {'after': after}
    response = get(URL, headers=head, allow_redirects=False,
                   params=parameters)
