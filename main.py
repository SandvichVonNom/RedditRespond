import praw
import pprint
import time
import string
import random

user = "h4h4-1"
pw = "123door"
prawWords = ['rito']
customsub = "ThePiickleBotSub"
customcomment = "rito XD rito XD rito XD rito XD rito XD rito XD rito XD rito XD rito XD rito XD"

apistring = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10))

r = praw.Reddit(apistring)
r.login(user, pw)
already_done = []

while True:
  subreddit = r.get_subreddit(customsub)
  for submission in subreddit.get_new(limit=100):
    submission.downvote()
    title_text = submission.title.lower()
    op_text = submission.selftext.lower()
    for keyword in prawWords:
      if ((keyword in op_text) or (keyword in title_text)) and submission.id not in already_done:
	submission.add_comment(customcomment)
	pprint.pprint(title_text)
	pprint.pprint(op_text)
	pprint.pprint(submission.short_link)
	time.sleep(601)
    
