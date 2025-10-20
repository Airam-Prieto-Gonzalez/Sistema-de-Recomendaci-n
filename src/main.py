from cli import parse_args
from fill import fill_matrix
from utils import print_matrix, read_matrix, print_similarity_table


def main():
    args = parse_args()
    matrix, min_score, max_score = read_matrix(args.file)
    filled_matrix, sim_matrix, neighbors_selected = fill_matrix(
        matrix,
        k=args.neighbors,
        metric=args.metric,
        method=args.type,
    )
    print("\nMatriz de utilidad completada:")
    print_matrix(filled_matrix)

    print_similarity_table(sim_matrix, args.metric)


if __name__ == "__main__":
    main()
