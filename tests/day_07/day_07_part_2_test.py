from problems.day_07 import day_07_part_2
from utils import read_lines_from_comment, read_lines_from_file


def test_day_07_part_2_example():
    example = """
        16,1,2,0,4,2,7,1,2,14
    """

    input = read_lines_from_comment(example)
    result = day_07_part_2.solve(input)

    assert 168 == result


def test_day_07_part_2_problem():
    input = read_lines_from_file(".\\data\\day_07\\day_07_input.txt")
    result = day_07_part_2.solve(input)

    assert 94017638 == result
