from problems.day_21 import day_21_part_2
from utils import read_lines_from_comment, read_lines_from_file


def test_day_21_part_2_example():
    example = """
        Player 1 starting position: 4
        Player 2 starting position: 8
    """

    input = read_lines_from_comment(example)
    result = day_21_part_2.solve(input)

    assert 444356092776315 == result


def test_day_21_part_2_problem():
    input = read_lines_from_file(".\\data\\day_21\\day_21_input.txt")
    result = day_21_part_2.solve(input)

    assert 193753136998081 == result
