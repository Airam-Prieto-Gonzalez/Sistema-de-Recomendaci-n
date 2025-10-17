from typing import List, Tuple


def read_matrix(file_path: str) -> Tuple[List[List[float]], float, float]:
    with open(file_path, "r") as f:
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
    for row in matrix:
        i = 0
        for e in row:
            row[i] = round(row[i], 2)
            i += 1
        print(row)
