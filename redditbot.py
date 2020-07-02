import praw
import time
import os
import re
import json

def bot_login():
    print("Logging in...")
    r = praw.Reddit('bot1')
    print("Logged in!")

    return r


def run_bot(r, comments_replied_to):
    print("Searching last 1,000 comments")

    wordlist= ['dance', 'dancing', 'dances', 'danced', 'disco', 'boogie', 'bop', 'tango', 'twerk']

    for comment in r.subreddit('all').comments(limit=1000):
        for word in wordlist:
            if re.search(r'\b{}\b'.format(word), comment.body) and comment.id not in comments_replied_to and comment.author != r.user.me() and comment.subreddit not in data['disallowed']:
                print("String with \"{}\" found in comment ".format(word) + comment.id)
                comment.reply('    Everyone, dance!\n\n----\n^^^I ^^^am ^^^a ^^^bot\n\n[Contact My Human](http://www.reddit.com/message/compose/?to=BokiTheCracker)')
                print("Replied to comment " + comment.id)

                comments_replied_to.append(comment.id)

                with open ("comments_replied_to.txt", "a") as f:
                    f.write(comment.id + "\n")

    print("Search Completed.")

    print(comments_replied_to)

    print("Sleeping for 10 seconds...")

    time.sleep(10)

def get_saved_comments():
    if not os.path.isfile("comments_replied_to.txt"):
        comments_replied_to = []
    else:
        with open("comments_replied_to.txt", "r") as f:
            comments_replied_to = f.read()
            comments_replied_to = comments_replied_to.split("\n")
            comments_replied_to = list(filter(None, comments_replied_to))

    return comments_replied_to

r = bot_login()
with open('subreddits.json') as f:
    data = json.load(f)
comments_replied_to = get_saved_comments()
print(comments_replied_to)
while True:
    run_bot(r, comments_replied_to)