import wikipedia
import os
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('insert token name here')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if '!search' in message.content:
        response = wikipedia.summary(message.content[8:])
        if len([char for char in response]) >= 2000:
            response = wikipedia.summary(message.content[8:], sentences=15)
            await message.channel.send(str(response))
        else:
            await message.channel.send(str(response))
    if '!help' in message.content:
        response = '!help to summon commands\n\n!search to search wikipedia\n\n!url to get wikipedia url'
        await message.channel.send(response)
    if  '!url' in message.content:
        response = wikipedia.page(message.content[5:]).url
        await message.channel.send(response)



client.run('insert bot token here')
