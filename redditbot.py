import praw
import time
import os
import re
import json

def bot_login():
    print("Logging in...")
    r = praw.Reddit(username=os.environ["reddit_username"],
                    password=os.environ["reddit_password"],
                    client_id=os.environ["client_id"],
                    client_secret=os.environ["client_secret"],
                    user_agent="PyEng Bot 0.1")
    print("Logged in!")

    return r


def run_bot(r):

    print("Searching last 1,000 comments")

    wordlist= ['dance', 'dancing', 'dances', 'danced', 'disco', 'boogie', 'bop', 'tango', 'twerk']

    for comment in r.subreddit('all').comments(limit=1000):
        for word in wordlist:
            if re.search(r'\b{}\b'.format(word), comment.body) and not comment.saved and comment.author != r.user.me() and comment.subreddit not in data['disallowed']:
                print("String with \"{}\" found in comment ".format(word) + comment.id)
                comment.reply('    Everyone, dance!\n\n----\n^^^I ^^^am ^^^a ^^^bot\n\n[Contact My Human](http://www.reddit.com/message/compose/?to=BokiTheCracker)')
                print("Replied to comment " + comment.id)



    print("Search Completed.")

    print("Sleeping for 60 seconds...")

    time.sleep(60)

r = bot_login()
with open('subreddits.json') as f:
    data = json.load(f)
for i in range(10):
    print(f"Iteration {i} out of 10")
    run_bot(r)