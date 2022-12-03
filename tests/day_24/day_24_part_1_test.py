from problems.day_24 import day_24_part_1
from utils import read_lines_from_file


def test_day_24_part_1_problem():
    input = read_lines_from_file(".\\data\\day_24\\day_24_input.txt")

    result = day_24_part_1.solve(input)
    assert 51939397989999 == result
