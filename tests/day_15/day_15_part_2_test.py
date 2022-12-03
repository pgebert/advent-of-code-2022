from problems.day_15 import day_15_part_2
from utils import read_lines_from_comment, read_lines_from_file


def test_day_15_part_2_example():
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
    result = day_15_part_2.solve(input)

    assert 315 == result


def test_day_15_part_2_problem():
    input = read_lines_from_file(".\\data\\day_15\\day_15_input.txt")
    result = day_15_part_2.solve(input)

    assert 2935 == result
