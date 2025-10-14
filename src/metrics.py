def pearson(matrix, user_u, user_v):
    common_items = [
        i
        for i in range(len(matrix[user_u]))
        if matrix[user_u][i] is not None and matrix[user_v][i] is not None
    ]

    if not common_items:
        return 0
    u_ratings = [r for r in matrix[user_u] if r is not None]
    v_ratings = [r for r in matrix[user_v] if r is not None]
    mean_u = sum(u_ratings) / len(u_ratings)
    mean_v = sum(v_ratings) / len(v_ratings)
    num = sum(
        (matrix[user_u][i] - mean_u) * (matrix[user_v][i] - mean_v)
        for i in common_items
    )
    denom_u = sum((matrix[user_u][i] - mean_u) ** 2 for i in common_items)
    denom_v = sum((matrix[user_v][i] - mean_v) ** 2 for i in common_items)

    denom = (denom_u**0.5) * (denom_v**0.5)
    return num / denom if denom != 0 else 0
