import os
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
client = discord.Client()

@client.event
async def on_ready():
    print (f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    # exit message parse if sender is a bot
    if message.author == client.user:
        return
    # parse message
    if message.content[0:6] == 'Wordle':
        response = "wordle message detected"
        await message.channel.send(response)

client.run(TOKEN)