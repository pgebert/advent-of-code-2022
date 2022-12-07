from problems.day_07 import day_07_part_1
from utils import read_lines_from_comment, read_lines_from_file


def test_day_07_part_1_example():
    example = """
        $ cd /
        $ ls
        dir a
        14848514 b.txt
        8504156 c.dat
        dir d
        $ cd a
        $ ls
        dir e
        29116 f
        2557 g
        62596 h.lst
        $ cd e
        $ ls
        584 i
        $ cd ..
        $ cd ..
        $ cd d
        $ ls
        4060174 j
        8033020 d.log
        5626152 d.ext
        7214296 k
    """

    input = read_lines_from_comment(example)
    result = day_07_part_1.solve(input)

    assert result == 95437


def test_day_07_part_1_problem():
    input = read_lines_from_file(".\\data\\day_07\\day_07_input.txt")
    result = day_07_part_1.solve(input)

    assert result == 1555642
