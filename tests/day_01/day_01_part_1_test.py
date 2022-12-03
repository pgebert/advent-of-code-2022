import os

from problems.day_01 import day_01_part_1
from utils import read_lines_from_comment, read_lines_from_file


def test_day_01_part_1_example():
    example = """
        1000
        2000
        3000
        
        4000
        
        5000
        6000
        
        7000
        8000
        9000
        
        10000
    """

    input = read_lines_from_comment(example, True)
    result = day_01_part_1.solve(input)

    assert 1532 == result


def test_day_01_part_1_problem():
    input = read_lines_from_file("..\\..\\data\\day_01\\day_01_input.txt", True)
    result = day_01_part_1.solve(input)

    assert 72718 == result
