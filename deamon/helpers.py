import numpy as np


def load_rating_matrix(db_scan, id_items, id_users):

    id_items = {v: i for i, v in enumerate(id_items)}
    id_users = {v: i for i, v in enumerate(id_users)}

    rating_matrix = np.zeros((len(id_users), len(id_items)))

    for id_item, id_user, rating in db_scan():
        rating_matrix[id_users[id_user], id_items[id_item]] = rating

    return rating_matrix
