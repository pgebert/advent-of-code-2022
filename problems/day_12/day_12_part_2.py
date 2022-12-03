from typing import List

from .graph import Graph

"""

https://adventofcode.com/2021/day/12

"""


def solve(input: List[str]):
    graph = Graph(input)
    paths = graph.find_paths(small_cave_penalty=True)
    return len(paths)
