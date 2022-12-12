"""

https://adventofcode.com/2022/day/12



"""

import string
from sys import maxsize
from typing import List


def toInt(character: str) -> int:
    if character == "S":
        return 1
    elif character == "E":
        return 26

    return string.ascii_letters.index(character) + 1


class Area:

    def __init__(self, input: List[str]):
        self.matrix = []
        self.starts = []
        self.destination = (0, 0)

        for row, line in enumerate(input):
            self.matrix.append([toInt(s) for s in line])

            for col, character in enumerate(line):
                if character == "S" or character == "a":
                    self.starts.append((row, col))
                elif character == "E":
                    self.destination = (row, col)

    def cost_to_destionation(self):

        min_path = maxsize
        destination_row, destination_col = self.destination

        for i, (start_row, start_col) in enumerate(self.starts):

            cost = []
            for row in self.matrix:
                cost.append([maxsize for _ in row])

            cost[start_row][start_col] = 0

            while True:
                changed = False
                for y in range(len(self.matrix)):
                    for x in range(len(self.matrix[y])):

                        if x == 0 and y == 0:
                            continue

                        updated_cost = 1 + min(
                            cost[y - 1][x] if y > 0 and self.matrix[y - 1][x] >= self.matrix[y][x] - 1 else maxsize,

                            cost[y][x - 1] if x > 0 and self.matrix[y][x - 1] >= self.matrix[y][x] - 1 else maxsize,
                            cost[y + 1][x] if y < len(self.matrix) - 1 and self.matrix[y + 1][x] >= self.matrix[y][
                                x] - 1 else maxsize,
                            cost[y][x + 1] if x < len(self.matrix[y]) - 1 and self.matrix[y][x + 1] >= self.matrix[y][
                                x] - 1 else maxsize
                        )

                        if updated_cost < cost[y][x]:
                            cost[y][x] = updated_cost
                            changed = True

                if not changed:
                    break

            if (new_min_path := cost[destination_row][destination_col]) < min_path:
                min_path = new_min_path

            print(f"{i + 1} from {len(self.starts)}: min path: {min_path}")

        return min_path


def solve(input: List[str]):
    area = Area(input)
    path = area.cost_to_destionation()
    return path
