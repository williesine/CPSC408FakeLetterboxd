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
    #channel = client.get_channel(1098666455215652877)
    if (message.content.startswith("!popcorn")):

        #we want the help menu to display options for each command and how to use it
        if (message.content == "!popcorn help"):
            await message.channel.send('''
            **Help Menu:**
            Option 1
            Option 2
            Option 3
            ''')

        # possible options:
        # view ratings by user
            # !popcorn reviews <username> <number of reviews to show>
                # displays only scores
                # show at the top how many reviews the user has made (to get the aggregation/group-by clause requirement)
            # !popcorn review <username> <movie/TVShow name>
                # displays score and text
        # view production attributes
            # !popcorn attribute <movie/TVShow name>
            # displays list of options, we can use the helper.get_choice() function from the previous assignments/labs
        # create a review
            # !popcorn create review <score 1-5> <text>
            # we don't want the user to use "" in case they use those characters in the review itself
        # update a review
            # !popcorn update review <movie/TVShow name> <score> <text>
            # prompt the user if they want to update score
            # prompt the user if they want to update review text
        # view top movies/TVShows
            # !popcorn top rated movies <number of results>
            # !popcorn top rated TV <number of results>
        # generate random movie/TVShow
            # !popcorn random <movie/TVShow>

        # what we still need :
            # two queries must involve joins across at least 3 tables
            # one query must contain a subquerys
client.run(TOKEN)