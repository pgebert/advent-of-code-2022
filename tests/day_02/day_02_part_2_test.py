from problems.day_02 import day_02_part_2
from utils import read_lines_from_comment, read_lines_from_file


def test_day_02_part_2_example():
    example = """
        forward 5
        down 5
        forward 8
        up 3
        down 8
        forward 2
    """

    input = read_lines_from_comment(example)
    result = day_02_part_2.solve(input)

    assert 900 == result


def test_day_02_part_2_problem():
    input = read_lines_from_file("..\\..\\data\\day_02\\day_02_input.txt")
    result = day_02_part_2.solve(input)

    assert 1781819478 == result
