from problems.day_15 import day_15_part_1
from utils import read_lines_from_comment, read_lines_from_file


def test_day_15_part_1_example():
    example = """
        1163751742
        1381373672
        2136511328
        3694931569
        7463417111
        1319128137
        1359912421
        3125421639
        1293138521
        2311944581
    """

    input = read_lines_from_comment(example)
    result = day_15_part_1.solve(input)

    assert 40 == result


def test_day_15_part_1_problem():
    input = read_lines_from_file(".\\data\\day_15\\day_15_input.txt")
    result = day_15_part_1.solve(input)

    assert 602 == result
