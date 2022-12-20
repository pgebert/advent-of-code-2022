from problems.day_20 import day_20_part_2
from utils import read_lines_from_comment, read_lines_from_file


def test_day_20_part_2_example():
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
    result = day_20_part_2.solve(input)

    assert result == 1623178306


def test_day_20_part_2_problem():
    input = read_lines_from_file(".\\data\\day_20\\day_20_input.txt")
    result = day_20_part_2.solve(input)

    assert result == 12374299815791
