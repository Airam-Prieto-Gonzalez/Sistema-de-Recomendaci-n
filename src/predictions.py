def predict_simple(matrix, similarity_matrix, user_idx, item_idx, neighbors):
    if not neighbors:
        return None
    num = sum(
        similarity_matrix[user_idx][n] * matrix[n][item_idx]
        for n in neighbors
        if matrix[n][item_idx] is not None
    )
    den = sum(
        abs(similarity_matrix[user_idx][n])
        for n in neighbors
        if matrix[n][item_idx] is not None
    )
    return num / den if den != 0 else None


def predict_mean(matrix, similarity_matrix, user_idx, item_idx, neighbors):
    if not neighbors:
        return None
    user_ratings = [value for value in matrix[user_idx] if value is not None]
    user_mean = sum(user_ratings) / len(user_ratings)
    num = 0
    denom = 0
    for n in neighbors:
        neighbor_ratings = matrix[n]
        sim = similarity_matrix[user_idx][n]
        neighbor_values = [value for value in neighbor_ratings if value is not None]
        if not neighbor_values:
            continue
        neighbor_mean = sum(neighbor_values) / len(neighbor_values)
        if neighbor_ratings[item_idx] is not None:
            num += sim * (neighbor_ratings[item_idx] - neighbor_mean)
            denom += abs(sim)

    return user_mean + num / denom if denom > 0 else user_mean
