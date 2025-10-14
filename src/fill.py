import numpy as np

from metrics import cosine, euclidean, pearson
from predictions import predict_mean_difference, predict_simple


def fill_matrix(matrix, k, metric="pearson", method="simple"):
    similarity_matrix = create_similarity_matrix(matrix, metric)
    n_users = len(matrix)
    n_items = len(matrix[0])
    filled_matrix = matrix.copy()
    neighbors_selected = []
    for i in range(n_users):
        for j in range(n_items):
            if matrix[i][j] is None:
                neighbors = get_top_k_neighbors(similarity_matrix, i, k)
                neighbors_selected.append(neighbors)
                if method == "simple":
                    matrix[i][j] = predict_simple(
                        filled_matrix, similarity_matrix, i, j, neighbors
                    )
                elif method == "mean_difference":
                    matrix[i][j] = predict_mean_difference(
                        filled_matrix, similarity_matrix, i, j, neighbors
                    )
                else:
                    pass
    return filled_matrix, similarity_matrix, neighbors_selected


def create_similarity_matrix(matrix, metric):
    n = len(matrix)
    similarity_matrix = np.zeros((n, n), dtype=float)
    for i in range(n):
        for j in range(n):
            if i != j:
                if metric == "pearson":
                    similarity_matrix[i][j] = pearson(matrix, i, j)
                elif metric == "cosine":
                    similarity_matrix[i][j] = cosine(matrix[i], matrix[j])
                elif metric == "euclidean":
                    similarity_matrix[i][j] = euclidean(matrix[i], matrix[j])
    return similarity_matrix


def get_top_k_neighbors(similarity_matrix, user_idx, k):
    sims = similarity_matrix[user_idx]
    neighbors = np.argsort(sims)[::-1][:k]
    return neighbors.tolist()
