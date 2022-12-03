import os

from problems.day_01 import day_01_part_1
from utils import read_lines_from_comment, read_lines_from_file


def test_day_01_part_1_example():
    example = """
        199
        200
        208
        210
        200
        207
        240
        269
        260
        263
    """

    input = read_lines_from_comment(example)
    result = day_01_part_1.solve(input)

    assert 7 == result


def test_day_01_part_1_problem():
    input = read_lines_from_file("..\\..\\data\\day_01\\day_01_input.txt")
    result = day_01_part_1.solve(input)

    assert 1532 == result
