from problems.day_11 import day_11_part_1
from utils import read_lines_from_comment, read_lines_from_file


def test_day_11_part_1_example():
    example = """
    Monkey 0:
      Starting items: 79, 98
      Operation: new = old * 19
      Test: divisible by 23
        If true: throw to monkey 2
        If false: throw to monkey 3
    
    Monkey 1:
      Starting items: 54, 65, 75, 74
      Operation: new = old + 6
      Test: divisible by 19
        If true: throw to monkey 2
        If false: throw to monkey 0
    
    Monkey 2:
      Starting items: 79, 60, 97
      Operation: new = old * old
      Test: divisible by 13
        If true: throw to monkey 1
        If false: throw to monkey 3
    
    Monkey 3:
      Starting items: 74
      Operation: new = old + 3
      Test: divisible by 17
        If true: throw to monkey 0
        If false: throw to monkey 1
    """

    input = read_lines_from_comment(example)
    result = day_11_part_1.solve(input)

    assert result == 10605


def test_day_11_part_1_problem():
    input = read_lines_from_file(".\\data\\day_11\\day_11_input.txt")
    result = day_11_part_1.solve(input)

    assert result == 55216
