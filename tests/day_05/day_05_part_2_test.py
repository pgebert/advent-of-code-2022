from problems.day_05 import day_05_part_2
from utils import read_lines_from_comment, read_lines_from_file


def test_day_05_part_2_example():
    example = """
        0,9 -> 5,9
        8,0 -> 0,8
        9,4 -> 3,4
        2,2 -> 2,1
        7,0 -> 7,4
        6,4 -> 2,0
        0,9 -> 2,9
        3,4 -> 1,4
        0,0 -> 8,8
        5,5 -> 8,2
    """

    input = read_lines_from_comment(example)
    result = day_05_part_2.solve(input)

    assert 12 == result


def test_day_05_part_2_problem():
    input = read_lines_from_file(".\\data\\day_05\\day_05_input.txt")
    result = day_05_part_2.solve(input)

    assert 19571 == result
