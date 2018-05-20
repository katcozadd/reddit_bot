import praw #importing the reddit API
import os #importing miscellaneous operating systems
import time #importing time access and conversions
import re #importing regular expressions operator


class RedditBot():


	def authenticate():
    """Authenticating User"""
    print('Authenticating...\n')
    reddit = praw.Reddit('MomBot', user_agent = 'web:MomBot:v0.1 (by /u/kittycozmo)')
    print('Authenticated as {}\n'.format(reddit.user.me()))
    return reddit
