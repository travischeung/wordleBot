import os
import discord
from dotenv import load_dotenv
from googleSheetsReadWrite import *

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
client = discord.Client()

@client.event
async def on_ready():
    print (f'{client.user} has joined this cringe discord.')

@client.event
async def on_message(message):
    messageList = message.content.split()
    # exit message parse if sender is a bot
    if message.author == client.user:
        return
    # parse da message
    if messageList[0] == 'Wordle':
        sender = message.author.display_name.strip('\#')
        points = messageList[2][0]
        wordleNum = messageList[1]

        updateStatus = wordleDetected(sender, points, wordleNum)
        await message.channel.send(updateStatus)
        return

client.run(TOKEN)