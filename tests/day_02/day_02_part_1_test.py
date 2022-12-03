from problems.day_02 import day_02_part_1
from utils import read_lines_from_comment, read_lines_from_file


def test_day_02_part_1_example():
    example = """
        A Y
        B X
        C Z
    """

    input = read_lines_from_comment(example)
    result = day_02_part_1.solve(input)

    assert 15 == result


def test_day_02_part_1_problem():
    input = read_lines_from_file("..\\..\\data\\day_02\\day_02_input.txt")
    result = day_02_part_1.solve(input)

    assert 11603 == result
