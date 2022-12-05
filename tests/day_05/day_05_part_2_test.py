from problems.day_05 import day_05_part_2
from utils import read_lines_from_comment, read_lines_from_file


def test_day_05_part_2_example():
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
    result = day_05_part_2.solve(input)

    assert result == "MCD"


def test_day_05_part_2_problem():
    input = read_lines_from_file(".\\data\\day_05\\day_05_input.txt", strip=False)
    result = day_05_part_2.solve(input)

    assert result == "QRQFHFWCL"
