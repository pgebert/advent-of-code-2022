from problems.day_16 import day_16_part_2
from utils import read_lines_from_file


def test_day_16_part_2_example():
    assert 3 == day_16_part_2.solve('C200B40A82')
    assert 54 == day_16_part_2.solve('04005AC33890')
    assert 7 == day_16_part_2.solve('880086C3E88112')
    assert 9 == day_16_part_2.solve('CE00C43D881120')
    assert 1 == day_16_part_2.solve('D8005AC2A8F0')
    assert 0 == day_16_part_2.solve('F600BC2D8F')
    assert 0 == day_16_part_2.solve('9C005AC2F8F0')
    assert 1 == day_16_part_2.solve('9C0141080250320F1802104A08')


def test_day_16_part_2_problem():
    input = read_lines_from_file(".\\data\\day_16\\day_16_input.txt")
    assert 744953223228 == day_16_part_2.solve(input[0])
