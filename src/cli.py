"""Parser module."""

import argparse


def parse_args():
    """
    Parse command-line arguments for the collaborative filtering recommendation system.

    Arguments:
      -f, --file (str, required): Archivo de matriz de utilidad.
      -m, --metric (str, optional): Métrica de similitud (por defecto: pearson).
      -k, --neighbors (int, optional): Número de vecinos a considerar (por defecto: 2).
      -t, --type (str, optional): Tipo de predicción (simple o mean_difference).

    Returns
    -------
      argparse.Namespace: Parsed command-line arguments.
    """
    parser = argparse.ArgumentParser(
        description="Sistema de recomendación basado en filtrado colaborativo"
    )
    parser.add_argument(
        "-f",
        "--file",
        required=True,
        help="Archivo de matriz de utilidad",
    )
    parser.add_argument(
        "-m",
        "--metric",
        choices=["pearson"],
        default="pearson",
        help="Métrica de similitud (por defecto: pearson)",
    )
    parser.add_argument(
        "-k",
        "--neighbors",
        type=int,
        default=2,
        help="Número de vecinos a considerar (por defecto: 2)",
    )
    parser.add_argument(
        "-t",
        "--type",
        choices=["simple", "mean_difference"],
        default="simple",
        help="Tipo de predicción (simple o mean_difference)",
    )
    return parser.parse_args()
