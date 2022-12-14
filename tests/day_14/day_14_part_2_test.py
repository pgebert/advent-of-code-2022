from problems.day_14 import day_14_part_2
from utils import read_lines_from_comment, read_lines_from_file


def test_day_14_part_2_example():
    example = """
    498,4 -> 498,6 -> 496,6
    503,4 -> 502,4 -> 502,9 -> 494,9
    """

    input = read_lines_from_comment(example)
    result = day_14_part_2.solve(input)

    assert result == 93


def test_day_14_part_2_problem():
    input = read_lines_from_file(".\\data\\day_14\\day_14_input.txt")
    result = day_14_part_2.solve(input)

    assert result == 30214
