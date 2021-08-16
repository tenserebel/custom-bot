import praw
from praw.reddit import Subreddit 

reddit = praw.Reddit(client_id = "KXcDm5WDNKB4Bg",
                     client_secret = "PVjxUSxGwwSCb7WaUUYjxDY_llpdig",
                     username = "tenserebel",
                     password = "smita3010",
                     user_agent = "memes")


Subreddit = reddit.subreddit("memes")

top = Subreddit.top(limit = 5)

for submission in top:
    print(submission.title)
