"""

https://adventofcode.com/2022/day/12

--- Day 12: Hill Climbing Algorithm ---
You try contacting the Elves using your handheld device, but the river you're following must be too low to get a decent signal.

You ask the device for a heightmap of the surrounding area (your puzzle input). The heightmap shows the local area from above broken into a grid; the elevation of each square of the grid is given by a single lowercase letter, where a is the lowest elevation, b is the next-lowest, and so on up to the highest elevation, z.

Also included on the heightmap are marks for your current position (S) and the location that should get the best signal (E). Your current position (S) has elevation a, and the location that should get the best signal (E) has elevation z.

You'd like to reach E, but to save energy, you should do it in as few steps as possible. During each step, you can move exactly one square up, down, left, or right. To avoid needing to get out your climbing gear, the elevation of the destination square can be at most one higher than the elevation of your current square; that is, if your current elevation is m, you could step to elevation n, but not to elevation o. (This also means that the elevation of the destination square can be much lower than the elevation of your current square.)

For example:

Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi
Here, you start in the top-left corner; your goal is near the middle. You could start by moving down or right, but eventually you'll need to head toward the e at the bottom. From there, you can spiral around to the goal:

v..v<<<<
>v.vv<<^
.>vv>E^^
..v>>>^^
..>>>>>^
In the above diagram, the symbols indicate whether the path exits each square moving up (^), down (v), left (<), or right (>). The location that should get the best signal is still E, and . marks unvisited squares.

This path reaches the goal in 31 steps, the fewest possible.

What is the fewest steps required to move from your current position to the location that should get the best signal?



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
        self.destination = (0, 0)

        for row, line in enumerate(input):
            self.matrix.append([toInt(s) for s in line])
            if "S" in line:
                self.start = (row, line.index("S"))
            if "E" in line:
                self.destination = (row, line.index("E"))

    def access(self, start: Tuple[int, int], destionation: Tuple[int, int]) -> bool:
        return self.matrix[start[0]][start[1]] >= self.matrix[destionation[0]][destionation[1]] - 1

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

        destination_row, destination_col = self.destination
        return cost[destination_row][destination_col]


def solve(input: List[str]):
    area = Area(input)
    path = area.cost_to_destionation()
    return path
