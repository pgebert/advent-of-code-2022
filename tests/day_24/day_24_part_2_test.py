from problems.day_24 import day_24_part_2
from utils import read_lines_from_file


def test_day_24_part_2_problem():
    input = read_lines_from_file(".\\data\\day_24\\day_24_input.txt")

    result = day_24_part_2.solve(input)
    assert 11717131211195 == result
