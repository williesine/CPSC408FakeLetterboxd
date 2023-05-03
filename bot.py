# bot.py
import os
import discord
from dotenv import load_dotenv
import mysql.connector
from db_operations import db_operations
from helper import helper
load_dotenv()
db_ops = db_operations()
print('connected')
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
    cleanedString = message.content.strip()
    messageParts = cleanedString.split(' ')
    if (messageParts[0].lower() == '!popcorn'):
        print(messageParts)
        print(message.author)
        #we want the help menu to display options for each command and how to use it
        if (messageParts[1].lower() == 'help'):
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
        if (messageParts[1].lower() == 'reviews'):
            if (len(messageParts) == 2):
                # no username given, print the current user's
                username = str(message.author)
            else:
                username = messageParts[2]
            queryFindUserID = '''
            SELECT userID
            FROM users
            WHERE name = %s;
            '''
            userIDresults = db_ops.name_placeholder_query(queryFindUserID, [username])
            userID = userIDresults[0][0]
            if (len(userIDresults) == 0):
                await message.channel.send('User with username ' + username + ' not found. Try again')
                return

            queryNumReviews = '''
            SELECT COUNT(*) 
            FROM reviews
            WHERE userID = %s;
            '''
            numUserReviews = db_ops.name_placeholder_query(queryNumReviews, [userID])[0][0]
            await message.channel.send(username + ' has made **' + str(numUserReviews) + '** reviews!')
            # !popcorn review <username> <movie/TVShow name>
                # displays score and text


        # view production attributes
            # !popcorn attribute <movie/TVShow name>
            # displays list of options, we can use the helper.get_choice() function from the previous assignments/labs


        # create a review
            # !popcorn create review "<movie/TVShow name>" <score 1-5> <text>
            # we don't want the user to use "" in case they use those characters in the review itself
        if (messageParts[1] == 'create' and messageParts[2] == 'review'):
            productionName = messageParts[3]
            i = 3
            while not (messageParts[i].endswith('"')):
                i += 1
            if (i > 3):
                productionName = " ".join(messageParts[3:i + 1])
            userRating = messageParts[i + 1]
            reviewText = " ".join(messageParts[i + 2:])
            queryFindID = '''
            SELECT movieID
            FROM movies
            WHERE title = %s
            '''
            titlePlaceholder = [productionName.strip('"')]
            movieID = db_ops.name_placeholder_query(queryFindID, titlePlaceholder)
            if (len(movieID) == 0):
                movieID = -1
                queryFindID = '''
                SELECT tvShowID
                FROM tvShows
                WHERE title = %s
                '''
                tvShowID = db_ops.name_placeholder_query(queryFindID, titlePlaceholder)[0][0]
                print('TV SHOW')
            else:
                tvShowID = -1
            
            queryFindUserID = '''
            SELECT userID
            FROM users
            WHERE name = %s;
            '''
            userIDresults = db_ops.name_placeholder_query(queryFindUserID, [str(message.author)])
            userID = userIDresults[0][0]
            
            queryInsert = '''
            INSERT INTO reviews (text, tvShowID, movieID, userID, userRating) VALUES (%s, %s, %s, %s, %s);
            '''
            # reviewID, text, tvShowID, movieID, userID, userRating
            placeholders = [reviewText, tvShowID, movieID, userID, userRating]
            for i in placeholders:
                print(type(i))
            db_ops.name_placeholder_query(queryInsert, placeholders)
            db_ops.commit()



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