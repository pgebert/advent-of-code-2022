from problems.day_14 import day_14_part_2
from utils import read_lines_from_comment, read_lines_from_file


def test_day_14_part_2_example():
    example = """
        NNCB
        
        CH -> B
        HH -> N
        CB -> H
        NH -> C
        HB -> C
        HC -> B
        HN -> C
        NN -> C
        BH -> H
        NC -> B
        NB -> B
        BN -> B
        BB -> N
        BC -> B
        CC -> N
        CN -> C
    """

    input = read_lines_from_comment(example)
    result = day_14_part_2.solve(input)

    assert 2188189693529 == result


def test_day_14_part_2_problem():
    input = read_lines_from_file(".\\data\\day_14\\day_14_input.txt")
    result = day_14_part_2.solve(input)

    assert 2914365137499 == result
