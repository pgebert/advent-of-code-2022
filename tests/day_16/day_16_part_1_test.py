from problems.day_16 import day_16_part_1
from utils import read_lines_from_file


def test_day_16_part_1_example():
    assert 6 == day_16_part_1.solve('D2FE28')
    assert 16 == day_16_part_1.solve('8A004A801A8002F478')
    assert 12 == day_16_part_1.solve('620080001611562C8802118E34')
    assert 23 == day_16_part_1.solve('C0015000016115A2E0802F182340')
    assert 31 == day_16_part_1.solve('A0016C880162017C3686B18A3D4780')


def test_day_16_part_1_problem():
    input = read_lines_from_file(".\\data\\day_16\\day_16_input.txt")
    assert 957 == day_16_part_1.solve(input[0])
