from __future__ import annotations

from typing import List

from .paper import Paper

"""

https://adventofcode.com/2021/day/13

--- Part Two ---
Finish folding the transparent paper according to the instructions. The manual says the code is always eight capital letters.

What code do you use to activate the infrared thermal imaging camera system?

"""


def solve(input: List[str]):
    points = [line for line in input if not line.startswith("fold")]
    instructions = [line for line in input if line.startswith("fold")]

    paper = Paper(points)

    for instruction in instructions:
        paper.fold(instruction)

    print(paper)

    return paper.count_points()
