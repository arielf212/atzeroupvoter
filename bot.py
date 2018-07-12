import praw
import os

reddit = praw.Reddit(client_id = os.environ.get('ID') , client_secret = os.environ.get('SECRET') , user_agent = 'faf' , username = os.environ.get('USERNAME') , password = os.environ.get('PASSWORD'))
collective = reddit.subreddit('collectivecg')

for post in collective.new(limit = 100):
    if post.score <= 0:
        post.upvote()