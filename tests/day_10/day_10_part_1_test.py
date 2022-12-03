from problems.day_10 import day_10_part_1
from utils import read_lines_from_comment, read_lines_from_file


def test_day_10_part_1_example():
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
    result = day_10_part_1.solve(input)

    assert 26397 == result


def test_day_10_part_1_problem():
    input = read_lines_from_file(".\\data\\day_10\\day_10_input.txt")
    result = day_10_part_1.solve(input)

    assert 319329 == result
