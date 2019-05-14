import numpy as np


def distance(a, b, cosine=True):
    if cosine:
        la = np.sum(np.square(a)) ** 0.5
        lb = np.sum(np.square(b)) ** 0.5

        return 1 - (np.dot(a, b) / (la * lb))

    return np.sum(np.square(a - b))


def KNN(target_index, vectors, k=5, cosine=True):
    """
    Calculate the K nearest neighbors of the target item
    Work on columns (items)

    Params
    ======
    - target_index (int)   : Index of the target column
    - vectors (np.ndarray) : Numpy 2D array rows: item vector
    - k (int)              : Number of neighbors to return
    """
    # Array of best item [distance, item_id]
    best_items = [[np.inf, 0]] * k

    target_item = vectors[target_index]

    for item_id, item_vector in enumerate(vectors):
        if item_id == target_index:
            continue

        dist = distance(target_item, item_vector, cosine=cosine)

        if [dist, 0] < best_items[-1]:
            del best_items[-1]
            best_items.append([dist, item_id])
            best_items.sort()

    # Keep only item id
    best_items = np.array(best_items)
    best_items = best_items[:, 1].reshape(1, -1)[0].astype(int)

    return best_items
