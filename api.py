import discord
import praw
import random
from discord.ext import commands
from praw.models.listing.mixins import subreddit
import requests
import json
from aiohttp import request

url = "https://meme-api-python.herokuapp.com/gimme"

response = requests.get(url)
print(response)

data = response.text

parsed = json.loads(data)


subreddit = parsed['subreddit']
print(subreddit)
