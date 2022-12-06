from problems.day_06 import day_06_part_1
from utils import read_lines_from_file


def test_day_06_part_1_example():
    result = day_06_part_1.solve("mjqjpqmgbljsphdztnvjfqwrcgsmlb")
    assert result == 7

    result = day_06_part_1.solve("bvwbjplbgvbhsrlpgdmjqwftvncz")
    assert result == 5

    result = day_06_part_1.solve("nppdvjthqldpwncqszvftbrmjlhg")
    assert result == 6

    result = day_06_part_1.solve("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg")
    assert result == 10

    result = day_06_part_1.solve("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw")
    assert result == 11


def test_day_06_part_1_problem():
    input = read_lines_from_file(".\\data\\day_06\\day_06_input.txt")
    result = day_06_part_1.solve(input[0])

    assert result == 1707
