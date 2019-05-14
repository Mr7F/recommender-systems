from flask import Flask, render_template
import mysql.connector as mariadb


app = Flask(__name__)

mariadb_connection = mariadb.connect(
    user='python_user',
    password='S3cR37_p@ss0WrD_r@d0|/|',
    database='Recommendations'
)

cursor = mariadb_connection.cursor()


@app.route("/")
def index():
    movies_id = [
        79132, 1, 551, 3785, 3793, 5816, 74458, 104841,
        2087, 8957, 59315, 8961, 4993
    ]
    query = '''
        SELECT Movies.id_movie, Movies.image
        FROM Movies
        WHERE %s
    ''' % ' OR '.join(['id_movie=%i' % id for id in movies_id])

    cursor.execute(query)

    movies = [i for i in cursor.fetchall()]

    return render_template(
        'index.html.j2',
        img_url=None,
        title='Choose a movie',
        movies=movies,
        genres=[],
        year=''
    )


@app.route("/<int:id>")
def movie(id):

    cursor.execute('SELECT * FROM Movies WHERE id_movie=%s', (id,))

    for id_movie, title, img, genres, year in cursor.fetchall():

        req = '''
            SELECT Movies.id_movie, Movies.image FROM Movies
            RIGHT JOIN Recommendations ON Recommendations.id_movie=%s
            WHERE Movies.id_movie=Recommendations.id_recom
            ORDER BY position;
        '''

        cursor.execute(req, (id,))
        movies = [img for img in cursor.fetchall()]

        return render_template(
            'index.html.j2',
            img_url='static/images/%s' % img,
            title=title,
            movies=movies,
            genres=genres.split('|'),
            year=year
        )

    return 'Error, wrong id maybe...'


app.run(port=8888, debug=True)
