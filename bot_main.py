import discord
import praw
import random
from discord.ext import commands
import requests
import json
from aiohttp import request

from praw.reddit import Subreddit 


reddit = praw.Reddit(client_id = "KXcDm5WDNKB4Bg",
                     client_secret = "PVjxUSxGwwSCb7WaUUYjxDY_llpdig",
                     username = "tenserebel",
                     password = "smita3010",
                     user_agent = "memes",
                     check_for_async = False)



client = commands.Bot(command_prefix = ">")



@client.event
async def on_ready():
    print("bot is ready")

@client.command(aliases = ['c'])
async def clear(ctx, amount=2):
    await ctx.channel.purge(limit = amount)

@client.command(aliases = ['m'])
async def mess(ctx, member : discord.Member,*,message = "you are a bitch"):
    await member.send(message)

@client.command(name = "fact")
async def fact(ctx):#, animal:str):

    URL = "https://some-random-api.ml/facts/dog"

    async with request("GET", URL, headers={}) as response:
        if response.status == 200:
            data = await response.json()
            await ctx.send(data["fact"])
        else:
            await ctx.send("api not responding")    

@client.command()
async def meme(ctx, subred = "memes"):
    Subreddit = reddit.subreddit(subred)
    all_subs = []


    top = Subreddit.top(limit = 50)

    for submission in top:
        all_subs.append(submission)

    random_sub = random.choice(all_subs)

    name = random_sub.title
    url = random_sub.url

    em = discord.Embed(title = name)

    em.set_image(url = url)

    await ctx.send(embed = em) 

@client.command(name = 'meme1')
async def meme1(ctx):
    URL = "https://meme-api-python.herokuapp.com/gimme"

    response = requests.get(URL)
    data = response.text
    parsed = json.loads(data)

    name = parsed['title']
    url = parsed['url']

    em = discord.Embed(title=name)
    em.set_image(url =url)
    
    async with request("GET",URL, headers = {}) as response:
        if response.status == 200:
            await ctx.send(embed =em)
        else:
            await ctx.send("api is not responding")    




client.run("token")        
