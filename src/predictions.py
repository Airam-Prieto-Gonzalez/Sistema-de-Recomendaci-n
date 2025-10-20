def predict_simple(matrix, similarity_matrix, user_idx, item_idx, neighbors):
    if not neighbors:
        return None

    num = 0
    den = 0
    num_terms = []
    den_terms = []
    print(f"\nPrediciendo usuario {user_idx}, ítem {item_idx} (predicción simple)")

    for n in neighbors:
        rating = matrix[n][item_idx]
        sim = similarity_matrix[user_idx][n]
        if rating is not None:
            num += sim * rating
            den += abs(sim)
            num_terms.append(f"{sim:.3f}*{rating:.3f}")
            den_terms.append(f"|{sim:.3f}|")
            print(
                f"  Vecino {n}: rating={rating:.3f}, sim={sim:.3f}, "
                f"num += sim*rating -> {num:.3f}, den += |sim| -> {den:.3f}"
            )

    if den != 0:
        formula_str = (
            f"predicción = ({' + '.join(num_terms)}) / ({' + '.join(den_terms)})"
        )
        print(f"  Fórmula: {formula_str} = {num:.3f}/{den:.3f}")
        prediction = num / den
        print(f"  => Valor predicho: {prediction:.3f}\n")
        return prediction
    else:
        print("  => No hay vecinos con ratings válidos, no se puede predecir\n")
        return None


def predict_mean_difference(matrix, similarity_matrix, user_idx, item_idx, neighbors):
    if not neighbors:
        return None

    user_ratings = [value for value in matrix[user_idx] if value is not None]
    user_mean = sum(user_ratings) / len(user_ratings)

    num = 0
    denom = 0
    num_terms = []
    den_terms = []
    print(
        f"\nPrediciendo usuario {user_idx}, ítem {item_idx} (diferencia con la media)"
    )
    print(f"  Media del usuario: {user_mean:.3f}")

    for n in neighbors:
        neighbor_ratings = matrix[n]
        neighbor_values = [v for v in neighbor_ratings if v is not None]
        if not neighbor_values:
            continue
        neighbor_mean = sum(neighbor_values) / len(neighbor_values)
        sim = similarity_matrix[user_idx][n]
        rating = neighbor_ratings[item_idx]
        if rating is not None:
            term = sim * (rating - neighbor_mean)
            num += term
            denom += abs(sim)
            num_terms.append(f"{sim:.3f}*({rating:.3f}-{neighbor_mean:.3f})")
            den_terms.append(f"|{sim:.3f}|")
            print(
                f"  Vecino {n}: rating={rating:.3f}, media_vecino={neighbor_mean:.3f}, "
                f"sim={sim:.3f}, num += sim*(rating-media) -> {num:.3f}, denom += |sim| -> {denom:.3f}"
            )

    if denom > 0:
        formula_str = f"predicción = {user_mean:.3f} + ({' + '.join(num_terms)}) / ({' + '.join(den_terms)})"
        prediction = user_mean + num / denom
        print(f"  Fórmula: {formula_str} = {prediction:.3f}")
    else:
        prediction = user_mean
        print(
            f"  => No hay vecinos válidos, predicción = media del usuario = {user_mean:.3f}"
        )

    print(f"  => Valor predicho: {prediction:.3f}\n")
    return prediction
