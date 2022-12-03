from problems.day_06 import day_06_part_1
from utils import read_lines_from_comment, read_lines_from_file


def test_day_06_part_1_example():
    example = """
        3,4,3,1,2
    """

    input = read_lines_from_comment(example)

    result = day_06_part_1.solve(input, 18)

    assert 26 == result

    result = day_06_part_1.solve(input, 80)

    assert 5934 == result


def test_day_06_part_1_problem():
    input = read_lines_from_file(".\\data\\day_06\\day_06_input.txt")
    result = day_06_part_1.solve(input, 80)

    assert 390923 == result
