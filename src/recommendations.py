def recommend_items(filled_matrix, n_recommendations=3):
    recommendations = {}
    for i, row in enumerate(filled_matrix):
        sorted_items = sorted(
            [(j, score) for j, score in enumerate(row)],
            key=lambda x: x[1],
            reverse=True,
        )
        top_items = [
            f"Ítem {idx} (predicción: {round(score, 2)})"
            for idx, score in sorted_items[:n_recommendations]
        ]
        recommendations[f"Usuario {i}"] = top_items
    return recommendations


def print_recommendations(recommendations):
    """Imprime las recomendaciones de forma legible."""
    print("\nRecomendaciones personalizadas:")
    for user, items in recommendations.items():
        print(f"\n{user}:")
        for item in items:
            print(f"  - {item}")
