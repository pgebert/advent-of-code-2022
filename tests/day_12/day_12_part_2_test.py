from problems.day_12 import day_12_part_2
from utils import read_lines_from_comment, read_lines_from_file


def test_day_11_part_2_example():
    example = """
        Sabqponm
        abcryxxl
        accszExk
        acctuvwj
        abdefghi
    """

    input = read_lines_from_comment(example)
    result = day_12_part_2.solve(input)

    assert result == 29


def test_day_12_part_2_problem():
    input = read_lines_from_file(".\\data\\day_12\\day_12_input.txt")
    result = day_12_part_2.solve(input)

    assert result == 377
