import yaml
from database import Database
from helpers import load_rating_matrix
from algorithms.autoencoder import Autoencoder

params = yaml.load(open('config.yaml', 'r').read())

database = Database(params)


def run_autoencoder():
    id_items = database.id_items()
    id_users = database.id_users()

    n_items = len(id_items)
    n_users = len(id_users)

    rating_matrix = load_rating_matrix(
        database.recommendations,
        id_items,
        id_users
    )

    print('%i users and %i items' % (n_users, n_items))

    autoencoder = Autoencoder(n_items, n_users)

    print('Training')
    autoencoder.train(rating_matrix)

    # Add recommendations
    print('Remove old prediction')
    database.clear_recommendations()
    print('Start insertion')
    for index, id_item in enumerate(id_items):
        print('Progression: %i / %i' % (index, n_items), end="\r")
        recoms = autoencoder.recommend(
            index,
            params['algorithm']['recommendations']
        )

        for position, recom in enumerate(recoms):
            database.add_recommendation(id_item, id_items[recom], position)

    print('Commit')
    database.mariadb_connection.commit()


if __name__ == '__main__':
    run_autoencoder()
