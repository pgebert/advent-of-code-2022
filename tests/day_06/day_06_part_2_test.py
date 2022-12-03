from problems.day_06 import day_06_part_2
from utils import read_lines_from_comment, read_lines_from_file


def test_day_06_part_2_example():
    example = """
        3,4,3,1,2
    """

    input = read_lines_from_comment(example)

    # result = day_06_part_2.solve(input, 2)
    # assert 6 == result
    #
    # result = day_06_part_2.solve(input, 6)
    # assert 10 == result
    #
    # result = day_06_part_2.solve(input, 7)
    # assert 10 == result

    result = day_06_part_2.solve(input, 10)
    assert 12 == result

    result = day_06_part_2.solve(input, 11)
    assert 15 == result

    result = day_06_part_2.solve(input, 18)
    assert 26 == result


def test_day_06_part_2_problem():
    input = read_lines_from_file(".\\data\\day_06\\day_06_input.txt")
    result = day_06_part_2.solve(input, 256)

    assert 1749945484935 == result
