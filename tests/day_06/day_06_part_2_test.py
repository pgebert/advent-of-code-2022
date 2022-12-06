from problems.day_06 import day_06_part_2
from utils import read_lines_from_file


def test_day_06_part_2_example():
    result = day_06_part_2.solve("mjqjpqmgbljsphdztnvjfqwrcgsmlb")
    assert result == 19

    result = day_06_part_2.solve("bvwbjplbgvbhsrlpgdmjqwftvncz")
    assert result == 23

    result = day_06_part_2.solve("nppdvjthqldpwncqszvftbrmjlhg")
    assert result == 23

    result = day_06_part_2.solve("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg")
    assert result == 29

    result = day_06_part_2.solve("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw")
    assert result == 26


def test_day_06_part_2_problem():
    input = read_lines_from_file(".\\data\\day_06\\day_06_input.txt")
    result = day_06_part_2.solve(input[0])

    assert result == 3697
