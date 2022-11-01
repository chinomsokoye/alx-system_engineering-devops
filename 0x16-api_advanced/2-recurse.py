#!/usr/bin/python3
"""
Returns lists containing titles of all hot articles
"""
from requests import get
from sys import argv


def recurse(subreddit, hot_list=[], after=None):
    """ Return list of hot articles """
    head = {'User-Agent': 'Avery Harper'}
    try:
        if after:
            count = get('https://www.reddit.com/r/{}/hot.json?after={}'.format(
                subreddit, after), headers=head).json().get('data')
        else:
            count = get('https://www.reddit.com/r/{}/hot.json'.format(
                subreddit), headers=head).json().get('data')
        hot_list += [dic.get('data').get('title')
                     for dic in count.get('children')]
        if count.get('after'):
            return recurse(subreddit, hot_list, after=count.get('after'))
        return hot_list
    except Exception:
        return None


if __name__ == "__main__":
    recurse(argv[1])
