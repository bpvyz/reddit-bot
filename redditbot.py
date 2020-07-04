import praw
import time
import os
import re
import json
import random
from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

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
            if re.search(fr'\b{word}\b', comment.body) and not comment.saved and comment.author != r.user.me() and comment.subreddit not in data['disallowed']:
                print(f"String with {word} found in comment {comment.id}")
                ascii = ascii_scrape(word)
                comment.reply(f'    Everyone, dance!\n\n\n{ascii}----\n^^^I ^^^am ^^^a ^^^bot\n\n[Contact My Human](http://www.reddit.com/message/compose/?to=BokiTheCracker)')
                print(f"Replied to comment {comment.id} with '{ascii}'")
    print("Search Completed.")
    print("Sleeping for 60 seconds...")
    time.sleep(60)

def ascii_scrape(word):
    driver = webdriver.Chrome(ChromeDriverManager().install())
    asciis = []
    driver.get(f"https://www.fastemoji.com/Search/?q={word}")
    content = driver.page_source
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