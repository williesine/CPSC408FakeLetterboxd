# bot.py
import os
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
intents = discord.Intents.default()
intents.message_content = True
intents.messages = True
intents.presences = True
intents.members = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    channel = client.get_channel(1098666455215652877)
    if (message.content.startswith("!popcorn")):
        await channel.send('hello!')
        if (message.content == "!popcorn help"):
            await channel.send('''
            **Help Menu:**
            Option 1
            Option 2
            Option 3
            ''')

client.run(TOKEN)