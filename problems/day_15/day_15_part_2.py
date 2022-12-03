from copy import deepcopy
from typing import List

from .cave import Cave

"""

https://adventofcode.com/2021/day/15


"""


def print_matrix(input):
    print()
    for line in input:
        print("".join(map(str, line)))


def increase_matrix_values(matrix, offset=1):
    matrix = deepcopy(matrix)

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            matrix[i][j] = matrix[i][j] + offset if matrix[i][j] + offset <= 9 else (matrix[i][j] + offset) % 9
    return matrix


def extend_matrix(matrix, factor):
    first_col = []
    for i in range(factor):
        for line in increase_matrix_values(matrix, i):
            first_col.append(line)
    new_matrix = deepcopy(first_col)
    for i in range(1, factor):
        for j, line in enumerate(increase_matrix_values(first_col, i)):
            new_matrix[j] += line
    return new_matrix


def solve(input: List[str]):
    input = [[int(s) for s in line] for line in input]
    input = extend_matrix(input, 5)

    cave = Cave(input)
    return cave.cost_to_destionation(iterations=10)
