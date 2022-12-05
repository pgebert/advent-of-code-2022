from problems.day_05 import day_05_part_1
from utils import read_lines_from_comment, read_lines_from_file


def test_day_05_part_1_example():
    example = """
            [D]    
        [N] [C]    
        [Z] [M] [P]
         1   2   3 
        
        move 1 from 2 to 1
        move 3 from 1 to 3
        move 2 from 2 to 1
        move 1 from 1 to 2
    """

    input = read_lines_from_comment(example, strip=False)
    result = day_05_part_1.solve(input)

    assert result == "CMZ"


def test_day_05_part_1_problem():
    input = read_lines_from_file(".\\data\\day_05\\day_05_input.txt", strip=False)
    result = day_05_part_1.solve(input)

    assert result == "TLFGBZHCN"
