
import mysql.connector as mariadb

mariadb_connection = mariadb.connect(
    user='python_user',
    password='S3cR37_p@ss0WrD_r@d0|/|',
    database='Recommendations'
)

cursor = mariadb_connection.cursor()


import pandas as pd
import re



'''

data = pd.read_csv('./MovieLens/ml-latest-small/movies.csv')

print(data.head())


def add_movies(movie_id, title, year, genres):
    cursor.execute("INSERT INTO Movies (id_movie, title, image, year, genres) VALUES (%s,%s,%s,%s,%s)",
    (movie_id, title, '%i.jpg'%movie_id, year, genres))


for index, row in data.iterrows():

    movie_id = row['movieId']
    m = re.search(r'(?<=\()[0-9]{4}', row['title'])
    if not m:
        print('Error on ', row['title'])
        year = '----'
    else:
        year = m.group(0)
    title = re.sub(r'\([0-9]{4}\)', '', row['title']).strip()
    genres = row['genres']

    add_movies(movie_id, title, year, genres)

print('Commit')
mariadb_connection.commit()
'''



data = pd.read_csv('./MovieLens/ml-latest-small/ratings.csv')
'''
print(data['userId'].unique().shape)

for id_user in data['userId'].unique():
    print(type(id_user))
    cursor.execute("INSERT INTO Users (id_user) VALUES (%i)" % id_user)

print('Commit')
mariadb_connection.commit()
'''

for index, row in data.iterrows():
    print(int(row['timestamp']))
    cursor.execute("INSERT INTO Ratings (id_user, id_movie, rating, timestamp) VALUES (%s,%s,%s,%s)" ,
        (int(row['userId']), int(row['movieId']), int(row['rating'] * 2), int(row['timestamp'])))
    print(index)

print('Commit')
mariadb_connection.commit()
