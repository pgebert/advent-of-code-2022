from problems.day_25 import day_25_part_1
from utils import read_lines_from_comment, read_lines_from_file


def test_day_25_part_1_example():
    example = """
        v...>>.vv>
        .vv>>.vv..
        >>.>v>...v
        >>v>>.>.v.
        v>v.vv.v..
        >.>>..v...
        .vv..>.>v.
        v.v..>>v.v
        ....v..v.>
    """

    input = read_lines_from_comment(example)
    result = day_25_part_1.solve(input)

    assert 58 == result


def test_day_25_part_1_problem():
    input = read_lines_from_file(".\\data\\day_25\\day_25_input.txt")
    result = day_25_part_1.solve(input)

    assert 389 == result
