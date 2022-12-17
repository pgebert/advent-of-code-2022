from problems.day_15 import day_15_part_2
from utils import read_lines_from_comment, read_lines_from_file


def test_day_15_part_2_example():
    example = """
    Sensor at x=2, y=18: closest beacon is at x=-2, y=15
    Sensor at x=9, y=16: closest beacon is at x=10, y=16
    Sensor at x=13, y=2: closest beacon is at x=15, y=3
    Sensor at x=12, y=14: closest beacon is at x=10, y=16
    Sensor at x=10, y=20: closest beacon is at x=10, y=16
    Sensor at x=14, y=17: closest beacon is at x=10, y=16
    Sensor at x=8, y=7: closest beacon is at x=2, y=10
    Sensor at x=2, y=0: closest beacon is at x=2, y=10
    Sensor at x=0, y=11: closest beacon is at x=2, y=10
    Sensor at x=20, y=14: closest beacon is at x=25, y=17
    Sensor at x=17, y=20: closest beacon is at x=21, y=22
    Sensor at x=16, y=7: closest beacon is at x=15, y=3
    Sensor at x=14, y=3: closest beacon is at x=15, y=3
    Sensor at x=20, y=1: closest beacon is at x=15, y=3
    """

    input = read_lines_from_comment(example)
    result = day_15_part_2.solve(input)

    assert result == 56000011


def test_day_15_part_2_problem():
    input = read_lines_from_file(".\\data\\day_15\\day_15_input.txt")
    result = day_15_part_2.solve(input)

    assert result == 13197439355220
