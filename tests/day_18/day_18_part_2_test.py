from problems.day_18 import day_18_part_2
from utils import read_lines_from_comment, read_lines_from_file


def test_day_18_part_2_example():
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
    result = day_18_part_2.solve(input)

    assert result == 58


def test_day_18_part_3_example():
    example = """
        2,2,2
        1,2,2
        3,2,2
        2,1,2
        2,3,2
        2,2,1
        2,2,3
        2,2,4
        2,2,7
        1,2,5
        3,2,5
        2,1,5
        2,3,5        
        1,2,6
        3,2,6
        2,1,6
        2,3,6
    """

    input = read_lines_from_comment(example)
    result = day_18_part_2.solve(input)

    assert result == 70


def test_day_18_part_2_problem():
    input = read_lines_from_file(".\\data\\day_18\\day_18_input.txt")
    result = day_18_part_2.solve(input)

    assert result == 2456
