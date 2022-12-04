from __future__ import annotations

from typing import List

from problems.day_04.Range import Range

"""

https://adventofcode.com/2022/day/4

--- Part Two ---
It seems like there is still quite a bit of duplicate work planned. Instead, the Elves would like to know the number of pairs that overlap at all.

In the above example, the first two pairs (2-4,6-8 and 2-3,4-5) don't overlap, while the remaining four pairs (5-7,7-9, 2-8,3-7, 6-6,4-6, and 2-6,4-8) do overlap:

5-7,7-9 overlaps in a single section, 7.
2-8,3-7 overlaps all of the sections 3 through 7.
6-6,4-6 overlaps in a single section, 6.
2-6,4-8 overlaps in sections 4, 5, and 6.
So, in this example, the number of overlapping assignment pairs is 4.

In how many assignment pairs do the ranges overlap?

"""


def solve(input: List[str]):
    contained_ranges = 0

    for line in input:
        first, second = [Range.fromString(string) for string in line.split(",")]

        if first.overlaps(second) or second.overlaps(first):
            contained_ranges += 1

    return contained_ranges
