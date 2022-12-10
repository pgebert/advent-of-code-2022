from __future__ import annotations

from typing import List

"""

https://adventofcode.com/2022/day/10


"""


def solve(input: List[str]):
    x = 1
    cycle = 0
    crt = []

    for i, line in enumerate(input):

        if line.startswith("noop"):
            cycle += 1

            normalized = cycle % 40
            pixel = "#" if x <= normalized <= x + 2 else "."
            crt.append(pixel)
        else:

            for _ in range(2):
                cycle += 1

                normalized = cycle % 40 if cycle % 40 != 0 else 40
                pixel = "#" if x <= normalized <= x + 2 else "."
                crt.append(pixel)

        if line.startswith("add"):
            x += int(line.split(" ")[1])

    print("\n")
    for i in range(6):
        print("".join(crt[i * 40: (i + 1) * 40]))
