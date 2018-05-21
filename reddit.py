import praw #importing the reddit API
import os #importing miscellaneous operating systems
import time #importing time access and conversions
import re #importing regular expressions operator


SUBREDDITS = ['test']

class RedditBot():

	def __init__(self, subreddits, path):
	"""Initialize the bot."""
	print("Initializing Bot")
	self.subreddits = subreddits
	self.path = path
	self.main()


	def authenticate():
    """Authenticating User"""
    print('Authenticating...\n')
    reddit = praw.Reddit('MomBot', user_agent = 'web:MomBot:v0.1 (by /u/kittycozmo)')
    print('Authenticated as {}\n'.format(reddit.user.me()))
    return reddit


	def main(self):
		"""Running the bot"""
		reddit = self.authenticate()
		while True:
			self.run_bot(reddit)