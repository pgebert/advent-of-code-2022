from problems.day_08 import day_08_part_1
from utils import read_lines_from_comment, read_lines_from_file


def test_day_08_part_1_example():
    example = """
        30373
        25512
        65332
        33549
        35390
    """

    input = read_lines_from_comment(example)
    result = day_08_part_1.solve(input)

    assert result == 21


def test_day_08_part_1_problem():
    input = read_lines_from_file(".\\data\\day_08\\day_08_input.txt")
    result = day_08_part_1.solve(input)

    assert result == 1845
