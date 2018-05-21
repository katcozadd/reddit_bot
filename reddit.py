import praw #importing the reddit API
import os #importing miscellaneous operating systems
import time #importing time access and conversions
import re #importing regular expressions operator


SUBREDDITS = ['test']

PATH = '/Users/katcozadd/Desktop/wdi-work/homework/reddit_bot/comments.txt'

class RedditBot():

	def __init__(self, subreddits, path):
		print("Initializing Bot")
		self.subreddits = subreddits
		self.path = path
		self.main()


	def authenticate(self):
	    print('Authenticating...\n')
	    reddit = praw.Reddit('MomBot', user_agent='web:reddit_bot:v0.1 (by /u/kittycozmo)')
	    print('Authenticated as {}\n'.format(reddit.user.me()))
	    return reddit

	def run_mom_bot(reddit, self):
		print('Getting 20 posts. \n')

		for submission in reddit.subreddit('+'.join(self.subs)).new(limit=20):

			for key, value in self.characters.items():

				match_title = re.findall(key, submission.title)
				if match_title:
					print(key + ' found in submission ID: ' + submission.id)

					if not os.path.exists(self.path):
						open(self.path, 'w').close()

					file_obj_r = open(self.path, 'r')

					if submission.id not in file_obj_r.read().splitlines():
						print('Link is unique. Posting comment.')

						try:
							comment = (
								'Hey mom, I appreciate you')

							submission.reply(comment)

						except praw.exceptions.APIException():
							print('Waiting 10 minutes. \n')
							time.sleep(600)
					else:
						print('Already replied. No reply needed. \n')

					time.sleep(10)

		print('Waiting 10 minutes. \n')
		time.sleep(600)


	def main(self):
		reddit = self.authenticate()
		while True:
			self.run_mom_bot(reddit)

mom_bot = RedditBot(SUBREDDITS, PATH)