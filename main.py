import discord
import random
import os
import requests
import json

from discord.ext import commands
from dotenv import load_dotenv

import modules.quote as quote

# load_dotenv reads from a file called .env in the same directory as the python files which should roughly look like BOT_TOKEN="1234567890"
load_dotenv()

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print("--- Bot is online and ready to interact! ---")
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')

@bot.command()
async def inspire(ctx):
    """
    command: !inspire
    Get a inspiration quote
    """
    inspire = quote.get_quote()
    await ctx.reply(inspire)

@bot.command()
async def hallo(ctx):
    """
    ctx - context (information about how the command was executed)
    command: !hallo
    """
    await ctx.send('Hee hallo! Welkom op de server')

@bot.command()
async def vliegavond(ctx):
    """
    command: !vliegavond
    """
    await ctx.send('Een lijst van de aankomende vliegdata is te vinden op: https://dutchdronesquad.nl/trainingen en hier vind je ook uitleg, hoe je kan aanmelden voor een vliegavond.')

@bot.command()
async def track(ctx):
    """
    command: !track
    """
    await ctx.send('Informatie over de huidige racetrack kan je vinden op: https://dutchdronesquad.nl/racetrack, of verken de track alvast in Velocidrone.')

@bot.event
async def on_message(message):
    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    print(f'{username}: {user_message} ({channel})')

    if message.author == bot.user:
        return

    # msg = message.content

    # if any(word in msg for word in sad_words):
    #     await message.reply(random.choice(happy_response))

    # Leave this here, otherwise commands wil stop running
    await bot.process_commands(message)

# run the bot using the token in .env
bot.run(os.environ['TOKEN'])