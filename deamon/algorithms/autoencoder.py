from algorithms.knn import KNN

from keras import Model
from keras.layers import Input, Embedding, Dense
import numpy as np


class Autoencoder:
    def __init__(self, n_items, n_users, k=80, verbose=True):
        self.n_users = n_users
        self.n_items = n_items
        self.k = k
        self.verbose = verbose
        self._compile()

    def _compile(self):
        layer_item_id = Input(shape=(1,), name='item_id')

        layer_item_vector_compressed = Embedding(self.n_items, self.k, name='items_vectors')

        layer_item_ratings = Dense(self.n_users)(layer_item_vector_compressed(layer_item_id))

        self.model = Model(layer_item_id, layer_item_ratings)

        self.model.compile('adam', 'mse')

    def train(self, rating_matrix, epochs=80):
        x_train = np.arange(self.n_items)
        y_train = rating_matrix.T.reshape(self.n_items, 1, self.n_users)

        self.model.fit(x=x_train, y=y_train, epochs=epochs, verbose=(1 if self.verbose else 0), validation_split=0)

        self.items_vectors = self.model.get_layer(name='items_vectors').get_weights()[0]

    def recommend(self, index_item, n):
        return KNN(index_item, self.items_vectors, n, cosine=False)
