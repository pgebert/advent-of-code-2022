from itertools import product
from typing import List

from .point import Point
from .utils import align_scanners, parse_input

"""

https://adventofcode.com/2021/day/19

--- Part Two ---
Sometimes, it's a good idea to appreciate just how big the ocean is. Using the Manhattan distance, how far apart do the scanners get?

In the above example, scanners 2 (1105,-1205,1229) and 3 (-92,-2380,-20) are the largest Manhattan distance apart. In total, they are 1197 + 1175 + 1249 = 3621 units apart.

What is the largest Manhattan distance between any two scanners?


"""


def distance_taxi(point_1: Point, point_2: Point) -> int:
    diff = point_1 - point_2
    return abs(diff.x) + abs(diff.y) + abs(diff.z)


def solve(input: List[str]):
    scanners = parse_input(input)
    scanners = align_scanners(scanners)

    distances = (distance_taxi(scanner_1.position, scanner_2.position)
                 for scanner_1, scanner_2 in product(scanners, repeat=2))

    return max(distances)
