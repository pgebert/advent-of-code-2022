from problems.day_23 import day_23_part_2
from utils import read_lines_from_comment, read_lines_from_file


def test_day_23_part_2_example():
    example = """
        #############
        #...........#
        ###B#C#B#D###
          #A#D#C#A#
          #########
    """

    input = read_lines_from_comment(example)
    result = day_23_part_2.solve(input)

    assert 44169 == result


def test_day_23_part_2_problem():
    input = read_lines_from_file(".\\data\\day_23\\day_23_input.txt")
    result = day_23_part_2.solve(input)

    assert 43117 == result
