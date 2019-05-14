# Recommender system
## Introduction
This work is part of my final thesis.
It is divided into two parts
1. The analysis of several recommendation algorithms, in terms of recommendation quality, memory and time complexity
2. A recommendation API, and an example website

## Comparison of different methods
In the python notebook, `Recommender systems - Comparison of different methods`, you will find my study of recommendation algorithms, using the [movielens](https://movielens.org) dataset.

## API
### Deamon
The recommendation API is used as a daemon.
This choice comes from comparing the different ways of offering a service, and it is more appropriate than a Rest API.

This API used the `auto-encoder` algorithm since it is the best algorithm at all levels.

You can configure the daemon with a yaml file.

Install the dependencies using pip
> pip install -r requirements.txt

Then, you should install MariaDB and load the database.

Then, you can add the daemon to a crontab.

### Demonstration website
The demonstration website was developed in python, using Flask.

You can also use a script the download the movie's images from [tmdb](https://www.themoviedb.org)
> python ./one_usage_tool/downoad_image.py

Then, run the website
> python ./website/index.py

### Report
You can also find my report, in French in the `report` folder.
