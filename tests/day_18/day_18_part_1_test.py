from problems.day_18 import day_18_part_1
from utils import read_lines_from_comment, read_lines_from_file


def test_day_18_part_1_example():
    example = """
        [[[0,[5,8]],[[1,7],[9,6]]],[[4,[1,2]],[[1,4],2]]]
        [[[5,[2,8]],4],[5,[[9,9],0]]]
        [6,[[[6,2],[5,6]],[[7,6],[4,7]]]]
        [[[6,[0,7]],[0,9]],[4,[9,[9,0]]]]
        [[[7,[6,4]],[3,[1,3]]],[[[5,5],1],9]]
        [[6,[[7,3],[3,2]]],[[[3,8],[5,7]],4]]
        [[[[5,4],[7,7]],8],[[8,3],8]]
        [[9,3],[[9,9],[6,[4,9]]]]
        [[2,[[7,7],7]],[[5,8],[[9,3],[0,2]]]]
        [[[[5,2],5],[8,[3,7]]],[[5,[7,5]],[4,4]]]
    """

    input = read_lines_from_comment(example)
    result = day_18_part_1.solve(input)

    assert 4140 == result


def test_day_18_part_1_problem():
    input = read_lines_from_file(".\\data\\day_18\\day_18_input.txt")
    result = day_18_part_1.solve(input)

    assert 3691 == result
