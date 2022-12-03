from problems.day_11 import day_11_part_1
from utils import read_lines_from_comment, read_lines_from_file


def test_day_11_part_1_example():
    example = """
        5483143223
        2745854711
        5264556173
        6141336146
        6357385478
        4167524645
        2176841721
        6882881134
        4846848554
        5283751526
    """

    input = read_lines_from_comment(example)

    result = day_11_part_1.solve(input, 10)

    assert 204 == result

    result = day_11_part_1.solve(input, 100)

    assert 1656 == result


def test_day_11_part_1_problem():
    input = read_lines_from_file("..\\..\\data\\day_11\\day_11_input.txt")
    result = day_11_part_1.solve(input, 100)

    assert 1640 == result
