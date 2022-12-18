from problems.day_18 import day_18_part_1
from utils import read_lines_from_comment, read_lines_from_file


def test_day_18_part_1_example_1():
    example = """
        1,1,1
        2,1,1
    """

    input = read_lines_from_comment(example)
    result = day_18_part_1.solve(input)

    assert result == 10


def test_day_18_part_1_example_2():
    example = """
        2,2,2
        1,2,2
        3,2,2
        2,1,2
        2,3,2
        2,2,1
        2,2,3
        2,2,4
        2,2,6
        1,2,5
        3,2,5
        2,1,5
        2,3,5
    """

    input = read_lines_from_comment(example)
    result = day_18_part_1.solve(input)

    assert result == 64


def test_day_18_part_1_problem():
    input = read_lines_from_file(".\\data\\day_18\\day_18_input.txt")
    result = day_18_part_1.solve(input)

    assert result == 4320
