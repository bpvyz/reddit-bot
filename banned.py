import praw
import json

def bot_login():
    print("Logging in...")
    r = praw.Reddit('bot1')
    print("Logged in!")
    return(r)

def update_banned(r):
    inbox = r.inbox.messages(limit=None)

    for message in inbox:
        if message.subject.startswith("You've been"):
            subreddit = message.subject.split()[-1]
            json_dump(subreddit)

def json_dump(subreddit):
    with open('subreddits.json') as f:
        data = json.load(f)
        if subreddit not in data['disallowed']:
            print(f"You've been banned from {subreddit}, appending to subreddits.json!")
            data['disallowed'].append(subreddit)
    with open('subreddits.json', 'w') as f:
        json.dump(data, f, sort_keys=True, indent=4)

update_banned(bot_login())