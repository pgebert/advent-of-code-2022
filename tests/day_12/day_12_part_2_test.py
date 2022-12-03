from problems.day_12 import day_12_part_2
from utils import read_lines_from_comment, read_lines_from_file


def test_day_11_part_2_example_small():
    example = """
        start-A
        start-b
        A-c
        A-b
        b-d
        A-end
        b-end
    """

    input = read_lines_from_comment(example)
    result = day_12_part_2.solve(input)

    assert 36 == result


def test_day_12_part_2_example_medium():
    example = """
        dc-end
        HN-start
        start-kj
        dc-start
        dc-HN
        LN-dc
        HN-end
        kj-sa
        kj-HN
        kj-dc
    """

    input = read_lines_from_comment(example)
    result = day_12_part_2.solve(input)

    assert 103 == result


def test_day_12_part_2_problem():
    input = read_lines_from_file(".\\data\\day_12\\day_12_input.txt")
    result = day_12_part_2.solve(input)

    assert 89592 == result
