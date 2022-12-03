from problems.day_10 import day_10_part_2
from utils import read_lines_from_comment, read_lines_from_file


def test_day_10_part_2_example():
    example = """
        [({(<(())[]>[[{[]{<()<>>
        [(()[<>])]({[<{<<[]>>(
        {([(<{}[<>[]}>{[]{[(<()>
        (((({<>}<{<{<>}{[]{[]{}
        [[<[([]))<([[{}[[()]]]
        [{[{({}]{}}([{[{{{}}([]
        {<[[]]>}<{[{[{[]{()[[[]
        [<(<(<(<{}))><([]([]()
        <{([([[(<>()){}]>(<<{{
        <{([{{}}[<[[[<>{}]]]>[]]
    """

    input = read_lines_from_comment(example)
    result = day_10_part_2.solve(input)

    assert 288957 == result


def test_day_10_part_2_problem():
    input = read_lines_from_file(".\\data\\day_10\\day_10_input.txt")
    result = day_10_part_2.solve(input)

    assert 3515583998 == result
