from typing import List, Tuple


def read_matrix(file_path: str) -> Tuple[List[List[float]], float, float]:
    with open(file_path, "r") as f:
        lines = [line.strip() for line in f.readlines() if line.strip()]

    min_score = float(lines[0])
    max_score = float(lines[1])
    matrix = []
    for line in lines[2:]:
        row = [float(x) if x != "-" else None for x in line.split()]
        matrix.append(row)
    return matrix, min_score, max_score


def print_matrix(matrix):
    for row in matrix:
        print(" ".join(f"{v:.2f}" if v is not None else "-" for v in row))
