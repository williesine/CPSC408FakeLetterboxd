from helper import helper
from db_operations import db_operations
dataCredits = helper.data_cleaner('credits.csv')
dataTitles = helper.data_cleaner('titles.csv')

db_ops = db_operations()

i = 1
while (i < len(dataTitles)):
    query = '''
        INSERT INTO titlesWhole VALUES (
            %s,
            %s,
            %s,
            %s,
            %s,
            %s,
            %s,
            %s,
            %s,
            %s,
            %s,
            %s,
            %s
        );
    '''
    print('7: ', len(dataTitles[i]))
    if (len(dataTitles[i]) == 4):
        print(dataTitles[i])
    if (dataTitles[i][7] is not None):
        genre = dataTitles[i][7].split('-')
        if (len(genre) == 0):
            genre = None
        else:
            genre = genre[0]
    else:
        genre = None

    if (dataTitles[i][8] is not None):
        production_country = dataTitles[i][8].split('-')
        if (len(production_country) == 0):
            production_country = None
        else:
            production_country = production_country[0]
    else:
        production_country = None
    
    print('genre: ', genre)
    print('production_country: ', production_country)
    placeholders = [dataTitles[i][0], dataTitles[i][1], dataTitles[i][2], dataTitles[i][3], dataTitles[i][4], dataTitles[i][5], dataTitles[i][6], genre, production_country, dataTitles[i][9], dataTitles[i][10], dataTitles[i][11], dataTitles[i][12]]
    db_ops.name_placeholder_query(query, placeholders)
    print(i)
    i += 1
db_ops.commit()



