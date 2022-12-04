from problems.day_04 import day_04_part_2
from utils import read_lines_from_comment, read_lines_from_file


def test_day_04_part_2_example():
    example = """
        2-4,6-8
        2-3,4-5
        5-7,7-9
        2-8,3-7
        6-6,4-6
        2-6,4-8
    """

    input = read_lines_from_comment(example)
    result = day_04_part_2.solve(input)

    assert result == 4


def test_day_04_part_2_problem():
    input = read_lines_from_file(".\\data\\day_04\\day_04_input.txt")
    result = day_04_part_2.solve(input)

    assert result == 909
