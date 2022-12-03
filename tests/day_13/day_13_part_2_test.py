from problems.day_13 import day_13_part_2
from utils import read_lines_from_comment, read_lines_from_file


def test_day_13_part_2_example_medium():
    example = """
        6,10
        0,14
        9,10
        0,3
        10,4
        4,11
        6,0
        6,12
        4,1
        0,13
        10,12
        3,4
        3,0
        8,4
        1,10
        2,14
        8,10
        9,0
        
        fold along y=7
        fold along x=5
    """

    input = read_lines_from_comment(example)
    result = day_13_part_2.solve(input)

    assert 16 == result


def test_day_13_part_2_problem():
    input = read_lines_from_file(".\\data\\day_13\\day_13_input.txt")
    result = day_13_part_2.solve(input)

    assert 102 == result
