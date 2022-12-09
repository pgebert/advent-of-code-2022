from problems.day_09 import day_09_part_1
from utils import read_lines_from_comment, read_lines_from_file


def test_day_09_part_1_example():
    example = """
    R 4
    U 4
    L 3
    D 1
    R 4
    D 1
    L 5
    R 2
    """

    input = read_lines_from_comment(example)
    result = day_09_part_1.solve(input)

    assert result == 13


def test_day_09_part_1_problem():
    input = read_lines_from_file(".\\data\\day_09\\day_09_input.txt")
    result = day_09_part_1.solve(input)

    assert result == 6314
