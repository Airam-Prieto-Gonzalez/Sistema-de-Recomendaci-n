def pearson(matrix, user_u, user_v):
    common_items = [
        i
        for i in range(len(matrix[user_u]))
        if matrix[user_u][i] is not None and matrix[user_v][i] is not None
    ]
    if not common_items:
        return 0.00
    u_vals = [matrix[user_u][i] for i in common_items]
    v_vals = [matrix[user_v][i] for i in common_items]
    mean_u = sum(u_vals) / len(u_vals)
    mean_v = sum(v_vals) / len(v_vals)
    num = sum((u - mean_u) * (v - mean_v) for u, v in zip(u_vals, v_vals))
    denom_u = sum((u - mean_u) ** 2 for u in u_vals)
    denom_v = sum((v - mean_v) ** 2 for v in v_vals)
    denom = (denom_u**0.5) * (denom_v**0.5)
    return num / denom if denom != 0 else 0.00


def cosine(matrix, user_u, user_v):
    common_items = [
        i
        for i in range(len(matrix[user_u]))
        if matrix[user_u][i] is not None and matrix[user_v][i] is not None
    ]
    if not common_items:
        return 0.00
    num = sum(matrix[user_u][i] * matrix[user_v][i] for i in common_items)
    denom_u = sum(matrix[user_u][i] ** 2 for i in common_items)
    denom_v = sum(matrix[user_v][i] ** 2 for i in common_items)
    denom = (denom_u**0.5) * (denom_v**0.5)
    return num / denom if denom != 0 else 0.00


def euclidean(matrix, user_u, user_v):
    common_items = [
        i
        for i in range(len(matrix[user_u]))
        if matrix[user_u][i] is not None and matrix[user_v][i] is not None
    ]
    if not common_items:
        return 0.00
    distance = 1 / (
        (sum((matrix[user_u][i] - matrix[user_v][i]) ** 2 for i in common_items)) ** 0.5
    )
    return distance
