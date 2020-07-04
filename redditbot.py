import praw
import time
import os
import re
import json
import random
from bs4 import BeautifulSoup
import requests

def bot_login():
    print("Logging in...")
    r = praw.Reddit('bot1')
    print("Logged in!")

    return r


def run_bot(r):
    print("Searching last 1,000 comments")
    wordlist= ['dance', 'dancing', 'dances', 'danced', 'disco', 'boogie', 'bop', 'tango', 'twerk']
    for comment in r.subreddit('all').comments(limit=1000):
        for word in wordlist:
            if re.search(fr'\b{word}\b', comment.body) and not comment.saved and comment.author != r.user.me() and comment.subreddit not in data['disallowed']:
                print(f"String with {word} found in comment {comment.id}")
                ascii = ascii_scrape(word)
                comment.reply(f'    Everyone, dance!\n\n\n{ascii}\n***\n^^^I ^^^am ^^^a ^^^bot\n\n[Contact My Human](http://www.reddit.com/message/compose/?to=BokiTheCracker)')
                print(f"Replied to comment {comment.id} with ascii: '{ascii}'")
    print("Search Completed.")
    print("Sleeping for 60 seconds...")
    time.sleep(5)

def ascii_scrape(word):
    page = requests.get(f"https://www.fastemoji.com/Search/?q={word}")
    asciis = []
    content = page.text
    soup = BeautifulSoup(content, "html.parser")
    for a in soup.findAll('div', attrs={'class':'box'}):
        ascii_list = a.findAll('span', attrs={'style': 'font-size: 1.5em;'})
        if ascii_list != []:
            for ascii in ascii_list:
                asciis.append(ascii.text)
    return(random.choice(asciis))

r = bot_login()
with open('subreddits.json') as f:
    data = json.load(f)
for i in range(7):
    print(f"Iteration {i+1} out of 7")
    run_bot(r)