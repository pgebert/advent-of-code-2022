from problems.day_21 import day_21_part_1
from utils import read_lines_from_comment, read_lines_from_file


def test_day_21_part_1_example():
    example = """
        root: pppw + sjmn
        dbpl: 5
        cczh: sllz + lgvd
        zczc: 2
        ptdq: humn - dvpt
        dvpt: 3
        lfqf: 4
        humn: 5
        ljgn: 2
        sjmn: drzm * dbpl
        sllz: 4
        pppw: cczh / lfqf
        lgvd: ljgn * ptdq
        drzm: hmdt - zczc
        hmdt: 32
    """

    input = read_lines_from_comment(example)
    result = day_21_part_1.solve(input)

    assert result == 152


def test_day_21_part_1_problem():
    input = read_lines_from_file(".\\data\\day_21\\day_21_input.txt")
    result = day_21_part_1.solve(input)

    assert result == 43699799094202
