from problems.day_17 import day_17_part_1
from utils import read_lines_from_comment, read_lines_from_file


def test_day_17_part_1_example():
    example = """
        target area: x=20..30, y=-10..-5
    """

    input = read_lines_from_comment(example)
    result = day_17_part_1.solve(input)

    assert 45 == result


def test_day_17_part_1_problem():
    input = read_lines_from_file(".\\data\\day_17\\day_17_input.txt")
    result = day_17_part_1.solve(input)

    assert 4005 == result
