from problems.day_03 import day_03_part_2
from utils import read_lines_from_comment, read_lines_from_file


def test_day_03_part_2_example():
    example = """
        00100
        11110
        10110
        10111
        10101
        01111
        00111
        11100
        10000
        11001
        00010
        01010
    """

    input = read_lines_from_comment(example)

    result = day_03_part_2.solve(input)
    assert 230 == result


def test_day_03_part_2_problem():
    input = read_lines_from_file(".\\data\\day_03\\day_03_input.txt")
    result = day_03_part_2.solve(input)

    assert 4406844 == result
