from problems.day_09 import day_09_part_2
from utils import read_lines_from_comment, read_lines_from_file


def test_day_09_part_2_example_1():
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
    result = day_09_part_2.solve(input)

    assert result == 1


def test_day_09_part_2_example_2():
    example = """
    R 5
    U 8
    L 8
    D 3
    R 17
    D 10
    L 25
    U 20
    """

    input = read_lines_from_comment(example)
    result = day_09_part_2.solve(input)

    assert result == 36


def test_day_09_part_2_problem():
    input = read_lines_from_file(".\\data\\day_09\\day_09_input.txt")
    result = day_09_part_2.solve(input)

    assert result == 2504
