from problems.day_09 import day_09_part_1
from utils import read_lines_from_comment, read_lines_from_file


def test_day_09_part_1_example():
    example = """
        2199943210
        3987894921
        9856789892
        8767896789
        9899965678
    """

    input = read_lines_from_comment(example)
    result = day_09_part_1.solve(input)

    assert 15 == result


def test_day_09_part_1_problem():
    input = read_lines_from_file(".\\data\\day_09\\day_09_input.txt")
    result = day_09_part_1.solve(input)

    assert 439 == result
