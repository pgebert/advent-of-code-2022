from problems.day_02 import day_02_part_2
from utils import read_lines_from_comment, read_lines_from_file


def test_day_02_part_2_example():
    example = """
        A Y
        B X
        C Z
    """

    input = read_lines_from_comment(example)
    result = day_02_part_2.solve(input)

    assert 12 == result


def test_day_02_part_2_problem():
    input = read_lines_from_file(".\\data\\day_02\\day_02_input.txt")
    result = day_02_part_2.solve(input)

    assert 12725 == result
