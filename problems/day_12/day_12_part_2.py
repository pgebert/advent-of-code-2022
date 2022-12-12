"""

https://adventofcode.com/2022/day/12

--- Part Two ---
As you walk up the hill, you suspect that the Elves will want to turn this into a hiking trail. The beginning isn't very scenic, though; perhaps you can find a better starting point.

To maximize exercise while hiking, the trail should start as low as possible: elevation a. The goal is still the square marked E. However, the trail should still be direct, taking the fewest steps to reach its goal. So, you'll need to find the shortest path from any square at elevation a to the square marked E.

Again consider the example from above:

Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi
Now, there are six choices for starting position (five marked a, plus the square marked S that counts as being at elevation a). If you start at the bottom-left square, you can reach the goal most quickly:

...v<<<<
...vv<<^
...v>E^^
.>v>>>^^
>^>>>>>^
This path reaches the goal in only 29 steps, the fewest possible.

What is the fewest steps required to move starting from any square with elevation a to the location that should get the best signal?

"""

import string
from sys import maxsize
from typing import List, Tuple


def toInt(character: str) -> int:
    if character == "S":
        return 1
    elif character == "E":
        return 26

    return string.ascii_letters.index(character) + 1


class Area:

    def __init__(self, input: List[str]):
        self.matrix = []
        self.start = (0, 0)
        self.destinations = []

        for row, line in enumerate(input):
            self.matrix.append([toInt(s) for s in line])

            for col, character in enumerate(line):
                if character == "S" or character == "a":
                    self.destinations.append((row, col))
                elif character == "E":
                    self.start = (row, col)

    def access(self, start: Tuple[int, int], destionation: Tuple[int, int]) -> bool:
        return self.matrix[start[0]][start[1]] <= self.matrix[destionation[0]][destionation[1]] + 1

    def cost_to_destionation(self):

        cost = []
        for row in self.matrix:
            cost.append([maxsize for _ in row])

        start_row, start_col = self.start
        cost[start_row][start_col] = 0

        while True:
            changed = False
            for y in range(len(self.matrix)):
                for x in range(len(self.matrix[y])):

                    if x == 0 and y == 0:
                        continue

                    updated_cost = 1 + min(
                        cost[y - 1][x] if y > 0 and self.access((y - 1, x), (y, x)) else maxsize,
                        cost[y][x - 1] if x > 0 and self.access((y, x - 1), (y, x)) else maxsize,
                        cost[y + 1][x] if y < len(self.matrix) - 1 and self.access((y + 1, x), (y, x)) else maxsize,
                        cost[y][x + 1] if x < len(self.matrix[y]) - 1 and self.access((y, x + 1), (y, x)) else maxsize
                    )

                    if updated_cost < cost[y][x]:
                        cost[y][x] = updated_cost
                        changed = True

            if not changed:
                break

        return min([cost[row][col] for row, col in self.destinations])


def solve(input: List[str]):
    area = Area(input)
    path = area.cost_to_destionation()
    return path
