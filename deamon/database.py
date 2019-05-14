import random
import mysql.connector as mariadb


class Database:
    def __init__(self, params):
        self.params = params

        self.mariadb_connection = mariadb.connect(
            user=params['database']['user'],
            password=params['database']['password'],
            database=params['database']['dbname']
        )

        self.cursor = self.mariadb_connection.cursor()

    def clear_recommendations(self):
        recomm_table = self.params['database']['recommendations_table']['name']
        self.cursor.execute('DELETE FROM %s' % recomm_table)

    def add_recommendation(self, id_item, id_recom, position):
        req = "INSERT INTO %s (%s, %s, %s) VALUES (%s, %s, %s)" % (
                self.params['database']['recommendations_table']['name'],
                self.params['database']['recommendations_table']['id_item'],
                self.params['database']['recommendations_table']['id_reco'],
                self.params['database']['recommendations_table']['position'],
                '%s', '%s', '%s'
                )

        self.cursor.execute(req, (id_item, id_recom, position))

    def recommendations(self):
        p = self.params['database']['ratings_table']

        self.cursor.execute('SELECT %s, %s, %s FROM %s' % (p['id_item'], p['id_user'], p['rating'], p['name']))

        return self.cursor.fetchall()

    def id_items(self):
        self.cursor.execute('SELECT %s FROM %s'%(self.params['database']['items_table']['id_item'],
                            self.params['database']['items_table']['name']))

        id_items = [id_item[0] for id_item in self.cursor.fetchall()]

        return id_items

    def id_users(self):
        self.cursor.execute('SELECT %s FROM %s'%(self.params['database']['users_table']['id_user'],
                            self.params['database']['users_table']['name']))

        id_items = [id_item[0] for id_item in self.cursor.fetchall()]

        return id_items

    def fill_randomly_recommendations(self, n=20):
        self.clear_recommendations()

        id_items = self.id_items()

        for id_item in id_items:
            for i, r in enumerate(random.sample(id_items, n)):
                self.add_recommendation(id_item, r, i)

        self.mariadb_connection.commit()
