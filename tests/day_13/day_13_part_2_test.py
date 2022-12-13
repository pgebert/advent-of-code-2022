from problems.day_13 import day_13_part_2
from utils import read_lines_from_comment, read_lines_from_file


def test_day_13_part_2_example_medium():
    example = """
    [1,1,3,1,1]
    [1,1,5,1,1]
    
    [[1],[2,3,4]]
    [[1],4]
    
    [9]
    [[8,7,6]]
    
    [[4,4],4,4]
    [[4,4],4,4,4]
    
    [7,7,7,7]
    [7,7,7]
    
    []
    [3]
    
    [[[]]]
    [[]]
    
    [1,[2,[3,[4,[5,6,7]]]],8,9]
    [1,[2,[3,[4,[5,6,0]]]],8,9]
    """

    input = read_lines_from_comment(example)
    result = day_13_part_2.solve(input)

    assert result == 140


def test_day_13_part_2_problem():
    input = read_lines_from_file(".\\data\\day_13\\day_13_input.txt")
    result = day_13_part_2.solve(input)

    assert result == 20383
