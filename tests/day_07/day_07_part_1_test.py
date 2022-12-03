from problems.day_07 import day_07_part_1
from utils import read_lines_from_comment, read_lines_from_file


def test_day_07_part_1_example():
    example = """
        16,1,2,0,4,2,7,1,2,14
    """

    input = read_lines_from_comment(example)
    result = day_07_part_1.solve(input)

    assert 37 == result


def test_day_07_part_1_problem():
    input = read_lines_from_file(".\\data\\day_07\\day_07_input.txt")
    result = day_07_part_1.solve(input)

    assert 333755 == result
