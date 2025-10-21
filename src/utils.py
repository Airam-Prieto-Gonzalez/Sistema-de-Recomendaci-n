from tabulate import tabulate
from termcolor import colored


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


def print_matrix(original_matrix, filled_matrix):
    """
    Imprime la matriz de utilidad completada en forma de tabla usando tabulate.
    Los valores predichos (originalmente '-') se muestran en rojo.
    """
    n_users = len(filled_matrix)
    n_items = len(filled_matrix[0])
    headers = [f"Ítem {j}" for j in range(n_items)]
    table = []
    for i in range(n_users):
        row = []
        for j in range(n_items):
            value = filled_matrix[i][j]
            if value is None:
                colored_value = colored("-", "red", attrs=["bold"])
            else:
                if original_matrix[i][j] is None:
                    colored_value = colored(f"{round(value, 2)}", "red", attrs=["bold"])
                else:
                    colored_value = f"{round(value, 2)}"
            row.append(colored_value)
        table.append(row)
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
