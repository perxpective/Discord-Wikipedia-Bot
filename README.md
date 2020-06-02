# Discord-Wikipedia-Bot
Add this bot to the server and let it help you get Wikipedia summaries and URLs on your server using the '!' prefix

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/perxpective/Discord-Wikipedia-Bot/)

Before getting into the code, I use the [Discord Developer Portal](https://discord.com/developers/applications) to create an application and bot to get the token and Client ID, so that I can connect the bot to run stipulated series of code later on.

## Initialisation
To start off, I initiate these modules to lay the foundations in order to set up a Discord client.

``` python
import wikipedia
import os
import discord
from dotenv import load_dotenv
```

Subsequently, I intialise the Discord bot via the `load_dontenv` function and `TOKEN` variable so that the Discord bot is able to connect and run the code and algorithms below.

``` python
load_dotenv()
TOKEN = os.getenv('insert_bot_token_here')
```
Finally, I initialise the `client` variable to set up the Discord bot.

`client = discord.Client()`

## Coding the Bot
> Before you do any coding, make sure you invite the bot to your own Discord server copying this link: https://discord.com/oauth2/authorize?client_id=IDHERE&scope=bot.
> Replace "IDHERE" in "client_id=IDHERE" with your own bot Client ID.
The following code below will output whether the Discord bot is connected to the server or not.

``` python
@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
```

The code below allows the bot to read user messages and respond in a manner as programmed.
``` python
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
```

The bot will respond to a ping if the user sends a message "!ping".
The user can retrieve Wikipedia summaries using the command "!search". This is done via the `wikipedia.summary()` function from the `wikipedia` module.

> Disclaimer: Some terms may not be searchable or the content is way too long to be messaged on your server's text channel. Thus, the bot is only programmed to send a maximum of 15 sentences from the Wikipedia summary. 

The user can retrieve Wikipedia URLs using the command "!url". This is done via the `wikipedia.page().url`

Finally, I run the Discord client
`client.run('insert bot token here')`

## Running the Bot
![screenshot](https://github.com/perxpective/Discord-Wikipedia-Bot/blob/master/dry%20run/Screenshot%202020-06-02%20at%2018.08.08.png)
![screenshot](https://github.com/perxpective/Discord-Wikipedia-Bot/blob/master/dry%20run/Screenshot%202020-06-02%20at%2018.08.20.png)
![screenshot](https://github.com/perxpective/Discord-Wikipedia-Bot/blob/master/dry%20run/Screenshot%202020-06-02%20at%2018.09.12.png)
![screenshot](https://github.com/perxpective/Discord-Wikipedia-Bot/blob/master/dry%20run/Screenshot%202020-06-02%20at%2018.09.59.png)
![screenshot](https://github.com/perxpective/Discord-Wikipedia-Bot/blob/master/dry%20run/Screenshot%202020-06-02%20at%2018.42.38.png)
