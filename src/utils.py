from tabulate import tabulate


def read_matrix(file_path: str) -> tuple[list[list[float]], float, float]:
    with open(file_path) as f:
        lines = [line.strip() for line in f.readlines() if line.strip()]

    min_score = float(lines[0])
    max_score = float(lines[1])
    matrix = []
    for line in lines[2:]:
        elements = line.split()
        row = []
        for element in elements:
            if element != "-":
                row.append(float(element))
            else:
                row.append(None)
        matrix.append(row)
    return matrix, min_score, max_score


def print_matrix(matrix):
    """
    Imprime la matriz de utilidad en formato de tabla, redondeada a 2 decimales.
    Los valores None se muestran como '-'.
    """
    n_users = len(matrix)
    n_items = len(matrix[0]) if matrix else 0

    headers = [f"Ítem {i}" for i in range(n_items)]
    table = []

    for _i, row in enumerate(matrix):
        formatted_row = [round(float(e), 2) if e is not None else "-" for e in row]
        table.append(formatted_row)

    print("\nMatriz de utilidad completada:")
    print(
        tabulate(
            table,
            headers=headers,
            showindex=[f"Usuario {i}" for i in range(n_users)],
            tablefmt="grid",
        )
    )


def print_similarity_table(sim_matrix, metric):
    """
    Imprime la matriz de similitud como tabla, con encabezados Usuario 0, Usuario 1, etc.
    """
    n = len(sim_matrix)
    headers = [f"Usuario {i}" for i in range(n)]
    table = []
    for i, row in enumerate(sim_matrix):
        rounded_row = [round(value, 2) for value in row]
        table.append(rounded_row)
    print(f"\nTabla de similitudes entre usuarios según la métrica {metric}:")
    print(
        tabulate(
            table,
            headers=headers,
            showindex=[f"Usuario {i}" for i in range(n)],
            tablefmt="grid",
        )
    )
