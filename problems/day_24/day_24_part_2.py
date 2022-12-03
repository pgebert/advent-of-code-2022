from typing import List

from .monad import monad

"""

https://adventofcode.com/2021/day/24

--- Part Two ---
As the submarine starts booting up things like the Retro Encabulator, you realize that maybe you don't need all these submarine features after all.

What is the smallest model number accepted by MONAD?

"""


def solve(program: List[str]):
    return monad(program, False)
