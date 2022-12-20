from problems.day_20 import day_20_part_1
from utils import read_lines_from_comment, read_lines_from_file


def test_day_20_part_1_example():
    example = """
        1
        2
        -3
        3
        -2
        0
        4
    """

    input = read_lines_from_comment(example)
    result = day_20_part_1.solve(input)

    assert result == 3


def test_day_20_part_1_problem():
    input = read_lines_from_file(".\\data\\day_20\\day_20_input.txt")
    result = day_20_part_1.solve(input)

    assert result < 14837
    assert result == 9866
