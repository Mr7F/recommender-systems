#!/usr/bin/python3
import urllib.request
import pandas as pd
import tmdbsimple as tmdb


data = pd.read_csv('./dataset/ml-latest-small/links.csv')

tmdb.API_KEY = '4df15aadc9a772800fc02345b6a0cd31'


def download_movie_image(tmdbId, filename):

    movie = tmdb.Movies(tmdbId)

    try:
        URL = 'http://image.tmdb.org/t/p/original' + movie.info()['poster_path']

    except Exception:
        print('Error for tmdbId == ', tmdbId)
        URL = 'https://www.keymusic.com/Content/images/keymusic/generic/image-not-found.jpg'

    urllib.request.urlretrieve(URL, filename + ".jpg")

    return URL


for index, row in data.iterrows():
    print(index, ' - ', row['movieId'])

    if index < 7336:
        continue

    download_movie_image(row['tmdbId'], './website/static/images/%i' % row['movieId'])

print('Finished')
