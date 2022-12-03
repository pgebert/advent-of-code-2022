from problems.day_12 import day_12_part_1
from utils import read_lines_from_comment, read_lines_from_file


def test_day_12_part_1_example():
    example = """
        start-A
        start-b
        A-c
        A-b
        b-d
        A-end
        b-end
    """

    input = read_lines_from_comment(example)
    result = day_12_part_1.solve(input)

    assert 10 == result


def test_day_12_part_1_problem():
    input = read_lines_from_file(".\\data\\day_12\\day_12_input.txt")
    result = day_12_part_1.solve(input)

    assert 3292 == result
