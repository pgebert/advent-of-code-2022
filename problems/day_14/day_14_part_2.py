from typing import List

from .polymer import Polymer

"""

https://adventofcode.com/2021/day/14

--- Part Two ---
The resulting polymer isn't nearly strong enough to reinforce the submarine. You'll need to run more steps of the pair insertion process; a total of 40 steps should do it.

In the above example, the most common element is B (occurring 2192039569602 times) and the least common element is H (occurring 3849876073 times); subtracting these produces 2188189693529.

Apply 40 steps of pair insertion to the polymer template and find the most and least common elements in the result. What do you get if you take the quantity of the most common element and subtract the quantity of the least common element?

"""


def solve(input: List[str]):
    most_common, least_common = Polymer(input).evolve(40)
    return most_common - least_common
