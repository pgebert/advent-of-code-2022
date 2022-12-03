from problems.day_03 import day_03_part_1
from utils import read_lines_from_comment, read_lines_from_file


def test_day_03_part_1_example():
    example = """
        vJrwpWtwJgWrhcsFMMfFFhFp
        jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
        PmmdzqPrVvPwwTWBwg
        wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
        ttgJtRGJQctTZtZT
        CrZsJsPPZsGzwwsLwLmpwMDw
    """

    input = read_lines_from_comment(example)
    result = day_03_part_1.solve(input)

    assert result == 157


def test_day_03_part_1_problem():
    input = read_lines_from_file(".\\data\\day_03\\day_03_input.txt")
    result = day_03_part_1.solve(input)

    assert result == 7875
